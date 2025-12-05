ALTER PROCEDURE AddAppointment
    @branch_id INT,
    @patient_cnic VARCHAR(13),
    @doctor_cnic VARCHAR(13),
    @status VARCHAR(20),
    @room_id INT,
    @assignment_start DATETIME,
    @assignment_end DATETIME
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @patient_id INT, @doctor_id INT, @appointment_id INT;

    -- Validate start and end time
    IF @assignment_start >= @assignment_end
    BEGIN
        RAISERROR('Assignment start time must be before end time.', 16, 1);
        RETURN;
    END

    -- Validate patient (any branch)
    SELECT @patient_id = patient_id
    FROM Patients
    WHERE cnic = @patient_cnic AND deleted = 0;

    IF @patient_id IS NULL
    BEGIN
        RAISERROR('Invalid patient CNIC', 16, 1);
        RETURN;
    END

    -- Validate doctor in the given branch
    SELECT @doctor_id = doctor_id
    FROM Doctors
    WHERE cnic = @doctor_cnic AND branch_id = @branch_id AND deleted = 0;

    IF @doctor_id IS NULL
    BEGIN
        RAISERROR('Invalid doctor CNIC for this branch', 16, 1);
        RETURN;
    END

    -- Check if room exists in the branch and is not deleted
    IF NOT EXISTS (
        SELECT 1
        FROM Rooms
        WHERE room_id = @room_id AND branch_id = @branch_id AND deleted = 0
    )
    BEGIN
        RAISERROR('Invalid or deleted room for this branch.', 16, 1);
        RETURN;
    END

    -- Check time conflict only if current status is Scheduled
    IF @status = 'Scheduled'
    BEGIN
        IF EXISTS (
            SELECT 1
            FROM Room_Assignments RA
            JOIN Rooms R ON RA.room_id = R.room_id
            JOIN Appointments A ON RA.appointment_id = A.appointment_id
            WHERE RA.room_id = @room_id
              AND R.branch_id = @branch_id
              AND A.status = 'Scheduled'
              AND (
                    (@assignment_start >= RA.assignment_start AND @assignment_start < RA.assignment_end)
                 OR (@assignment_end > RA.assignment_start AND @assignment_end <= RA.assignment_end)
                 OR (RA.assignment_start >= @assignment_start AND RA.assignment_start < @assignment_end)
                 )
        )
        BEGIN
            RAISERROR('Room already assigned during this time in this branch (Scheduled only).', 16, 1);
            RETURN;
        END
    END

    -- Insert Appointment
    INSERT INTO Appointments (patient_id, doctor_id, status)
    VALUES (@patient_id, @doctor_id, @status);

    SET @appointment_id = SCOPE_IDENTITY();

    -- Insert Room Assignment
    INSERT INTO Room_Assignments (appointment_id, room_id, assignment_start, assignment_end)
    VALUES (@appointment_id, @room_id, @assignment_start, @assignment_end);
END
GO













ALTER PROCEDURE GetAppointments
    @doctor_cnic VARCHAR(13) = NULL,
    @patient_cnic VARCHAR(13) = NULL,
    @room_id INT = NULL,
    @status VARCHAR(20) = NULL
AS
BEGIN
    SET NOCOUNT ON;

    SELECT 
        A.appointment_id,
        P.first_name + ' ' + P.last_name AS patient_name,
        P.cnic AS patient_cnic,
        D.first_name + ' ' + D.last_name AS doctor_name,
        D.cnic AS doctor_cnic,
        A.status,
        RA.room_id,
        FORMAT(RA.assignment_start, 'yyyy-MM-dd hh:mm tt') AS assignment_start,
        FORMAT(RA.assignment_end, 'yyyy-MM-dd hh:mm tt') AS assignment_end,
        B.branch_name
    FROM Appointments A
    JOIN Patients P ON A.patient_id = P.patient_id
    JOIN Doctors D ON A.doctor_id = D.doctor_id
    JOIN Room_Assignments RA ON A.appointment_id = RA.appointment_id
    JOIN Branches B ON B.branch_id = D.branch_id
    WHERE 
        (@doctor_cnic IS NULL OR D.cnic LIKE @doctor_cnic + '%')
        AND (@patient_cnic IS NULL OR P.cnic LIKE @patient_cnic + '%')
        AND (@room_id IS NULL OR RA.room_id = @room_id)
        AND (@status IS NULL OR A.status = @status)
    ORDER BY RA.assignment_start;
END
GO