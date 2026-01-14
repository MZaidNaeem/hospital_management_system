USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[AddAppointment]    Script Date: 1/14/2026 7:20:01 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[AddAppointment]
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

    DECLARE 
        @patient_id INT, 
        @doctor_id INT, 
        @appointment_id INT;

    BEGIN TRY
        BEGIN TRANSACTION;

       

        -- Validate patient
        SELECT @patient_id = patient_id
        FROM Patients
        WHERE cnic = @patient_cnic AND deleted = 0;

        IF @patient_id IS NULL
        BEGIN
            RAISERROR('Invalid patient CNIC', 16, 1);
        END

        -- Validate doctor in branch
        SELECT @doctor_id = doctor_id
        FROM Doctors
        WHERE cnic = @doctor_cnic 
          AND branch_id = @branch_id 
          AND deleted = 0;

        IF @doctor_id IS NULL
        BEGIN
            RAISERROR('Invalid doctor CNIC for this branch', 16, 1);
        END

        -- Validate room
        IF NOT EXISTS (
            SELECT 1
            FROM Rooms
            WHERE room_id = @room_id 
              AND branch_id = @branch_id 
              AND deleted = 0
        )
        BEGIN
            RAISERROR('Invalid or deleted room for this branch.', 16, 1);
        END


        -- NEW CHECK: start time >= current datetime
        IF @assignment_start < GETDATE()
        BEGIN
            RAISERROR('Appointment start time cannot be in the past.', 16, 1);
        END

         -- Validate start and end time
        IF @assignment_start >= @assignment_end
        BEGIN
            RAISERROR('Assignment start time must be before end time.', 16, 1);
        END

        -- Check room time conflict (only Scheduled)
        IF @status = 'Scheduled'
        BEGIN
            IF EXISTS (
                SELECT 1
                FROM Room_Assignments RA
                JOIN Appointments A ON RA.appointment_id = A.appointment_id
                JOIN Rooms R ON RA.room_id = R.room_id
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
                RAISERROR('Room already assigned during this time (Scheduled).', 16, 1);
            END
        END

        -- Check doctor time conflict (only Scheduled)
        IF @status = 'Scheduled'
        BEGIN
            IF EXISTS (
                SELECT 1
                FROM Appointments A
                JOIN Room_Assignments RA
                    ON A.appointment_id = RA.appointment_id
                WHERE A.doctor_id = @doctor_id
                  AND A.status = 'Scheduled'
                  AND (
                        (@assignment_start >= RA.assignment_start AND @assignment_start < RA.assignment_end)
                     OR (@assignment_end > RA.assignment_start AND @assignment_end <= RA.assignment_end)
                     OR (RA.assignment_start >= @assignment_start AND RA.assignment_start < @assignment_end)
                  )
            )
            BEGIN
                RAISERROR('Doctor already has a scheduled appointment during this time.', 16, 1);
            END
        END



        -- Check patient time conflict (only Scheduled)
        IF @status = 'Scheduled'
        BEGIN
            IF EXISTS (
                SELECT 1
                FROM Appointments A
                JOIN Room_Assignments RA
                    ON A.appointment_id = RA.appointment_id
                WHERE A.patient_id = @patient_id
                  AND A.status = 'Scheduled'
                  AND (
                        (@assignment_start >= RA.assignment_start AND @assignment_start < RA.assignment_end)
                     OR (@assignment_end > RA.assignment_start AND @assignment_end <= RA.assignment_end)
                     OR (RA.assignment_start >= @assignment_start AND RA.assignment_start < @assignment_end)
                  )
            )
            BEGIN
                RAISERROR('Patient already has a scheduled appointment during this time.', 16, 1);
            END
        END




        -- Insert Appointment
        INSERT INTO Appointments (patient_id, doctor_id, status)
        VALUES (@patient_id, @doctor_id, @status);

        SET @appointment_id = SCOPE_IDENTITY();

        -- Insert Room Assignment
        INSERT INTO Room_Assignments
            (appointment_id, room_id, assignment_start, assignment_end)
        VALUES
            (@appointment_id, @room_id, @assignment_start, @assignment_end);

        COMMIT TRANSACTION;
    END TRY

    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;

        -- Return actual error
        DECLARE @ErrorMessage NVARCHAR(4000);
        SET @ErrorMessage = ERROR_MESSAGE();

        RAISERROR(@ErrorMessage, 16, 1);
    END CATCH
END


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[AddPatient]    Script Date: 1/14/2026 7:20:48 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[AddPatient]
    @first_name VARCHAR(255),
    @last_name VARCHAR(255),
    @Email VARCHAR(255),
    @CNIC VARCHAR(13),
    @Password VARCHAR(255),
    @Gender VARCHAR(50),
    @Contact VARCHAR(50),
    @Deleted BIT
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO Patients (
        first_name,
        last_name,
        email,
        cnic,
        password,
        gender,
        contact_number,
        created_at,
        deleted
    )
    VALUES (
        @first_name,
        @last_name,
        @Email,
        @CNIC,
        @Password,
        @Gender,
        @Contact,
        GETDATE(),
        @Deleted
    );
END


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[CompleteAppointment]    Script Date: 1/14/2026 7:20:59 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER   PROCEDURE [dbo].[CompleteAppointment]
    @appointment_id INT,
    @doctor_id INT
AS
BEGIN
    SET NOCOUNT ON;

    -- Only update if appointment belongs to doctor AND is scheduled
    UPDATE Appointments
    SET status = 'Completed'
    WHERE appointment_id = @appointment_id
      AND doctor_id = @doctor_id
      AND LOWER(status) = 'scheduled';

    -- Return number of rows affected
    SELECT @@ROWCOUNT AS rows_updated;
END


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[DeleteAdminProfile]    Script Date: 1/14/2026 7:21:24 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[DeleteAdminProfile]
    @admin_id INT
AS
BEGIN
    SET NOCOUNT ON;

    IF (SELECT COUNT(*) FROM admin) <= 1
    BEGIN
        -- Do not allow deleting the last admin
        RAISERROR ('Cannot delete the last remaining admin.', 16, 1);
        RETURN;
    END


    -- This DELETE will be intercepted by the trigger
    DELETE FROM admin
    WHERE admin_id = @admin_id;
END;


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[DeleteAppointment]    Script Date: 1/14/2026 7:21:32 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[DeleteAppointment]
    @appointment_id INT
AS
BEGIN
    SET NOCOUNT ON;

    BEGIN TRY
        BEGIN TRANSACTION;

        -- Check if appointment exists
        IF NOT EXISTS (
            SELECT 1 
            FROM Appointments 
            WHERE appointment_id = @appointment_id
        )
        BEGIN
            RAISERROR('Appointment not found.', 16, 1);
        END

        -- Delete related room assignments first
        DELETE FROM Room_Assignments
        WHERE appointment_id = @appointment_id;

        -- Delete the appointment
        DELETE FROM Appointments
        WHERE appointment_id = @appointment_id;

        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        -- Rollback if error occurs
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;

        -- Return the actual error
        DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
        DECLARE @ErrorSeverity INT = ERROR_SEVERITY();
        DECLARE @ErrorState INT = ERROR_STATE();

        RAISERROR (@ErrorMessage, @ErrorSeverity, @ErrorState);
    END CATCH
END


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[DeleteDoctorAccount]    Script Date: 1/14/2026 7:21:43 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[DeleteDoctorAccount]
    @doctor_id INT
AS
BEGIN
    UPDATE Doctors
    SET deleted = 1
    WHERE doctor_id = @doctor_id;
END;


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[GetAdminsExceptSelf]    Script Date: 1/14/2026 7:21:51 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER   PROCEDURE [dbo].[GetAdminsExceptSelf]
    @current_admin_id INT,
    @filter_cnic VARCHAR(50) = NULL   -- optional parameter
AS
BEGIN
    SET NOCOUNT ON;

    SELECT 
        a.admin_id, 
        a.first_name, 
        a.last_name, 
        a.email, 
        a.cnic, 
        a.password, 
        a.created_at, 
        a.deleted
    FROM Admin a
    WHERE 
        a.admin_id != @current_admin_id
        AND (
              @filter_cnic IS NULL 
              OR @filter_cnic = '' 
              OR a.cnic LIKE @filter_cnic + '%'
            )
    ORDER BY a.created_at DESC;
END


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[GetAppointments]    Script Date: 1/14/2026 7:22:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[GetAppointments]
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


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[GetBranches]    Script Date: 1/14/2026 7:22:18 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


ALTER PROCEDURE [dbo].[GetBranches]
AS
BEGIN
    SET NOCOUNT ON;

    SELECT 
        branch_id,
        branch_name,
        contact_number,
        created_at,
        deleted

    FROM Branches
END


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[GetBranchLevelReport]    Script Date: 1/14/2026 7:22:25 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[GetBranchLevelReport]
    @filter_type VARCHAR(10)   -- DAILY | WEEKLY | MONTHLY
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        b.branch_id   AS [Branch ID],
        b.branch_name AS [Branch Name],

        /* ===================== DOCTORS ===================== */

        -- Total Doctors
        (
            SELECT COUNT(*)
            FROM Doctors d
            WHERE d.branch_id = b.branch_id
              AND d.deleted = 0
        ) AS [Total Doctors],

        -- Active Doctors
        (
            SELECT COUNT(DISTINCT d.doctor_id)
            FROM Doctors d
            JOIN Appointments a ON a.doctor_id = d.doctor_id
            JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
            WHERE d.branch_id = b.branch_id
              AND d.deleted = 0
              AND a.status IN ('Completed','Scheduled')
              AND (
                    (@filter_type = 'DAILY'
                        AND ra.assignment_start >= CAST(GETDATE() AS DATE)
                        AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE))
                    )
                 OR (@filter_type = 'WEEKLY'
                        AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0)
                        AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0)
                    )
                 OR (@filter_type = 'MONTHLY'
                        AND MONTH(ra.assignment_start) = MONTH(GETDATE())
                        AND YEAR(ra.assignment_start) = YEAR(GETDATE())
                    )
              )
        ) AS [Active Doctors],

        -- Inactive Doctors
        (
            SELECT COUNT(*)
            FROM Doctors d
            WHERE d.branch_id = b.branch_id
              AND d.deleted = 0
              AND d.doctor_id NOT IN (
                    SELECT DISTINCT d2.doctor_id
                    FROM Doctors d2
                    JOIN Appointments a ON a.doctor_id = d2.doctor_id
                    JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
                    WHERE a.status IN ('Completed','Scheduled')
                      AND (
                            (@filter_type = 'DAILY'
                                AND ra.assignment_start >= CAST(GETDATE() AS DATE)
                                AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE))
                            )
                         OR (@filter_type = 'WEEKLY'
                                AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0)
                                AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0)
                            )
                         OR (@filter_type = 'MONTHLY'
                                AND MONTH(ra.assignment_start) = MONTH(GETDATE())
                                AND YEAR(ra.assignment_start) = YEAR(GETDATE())
                            )
                      )
              )
        ) AS [Inactive Doctors],

        /* ===================== ROOMS ===================== */

        -- Total Rooms
        (
            SELECT COUNT(*)
            FROM Rooms r
            WHERE r.branch_id = b.branch_id
              AND r.deleted = 0
        ) AS [Total Rooms],

        -- Active Rooms
        (
            SELECT COUNT(DISTINCT r.room_id)
            FROM Rooms r
            JOIN Room_Assignments ra ON ra.room_id = r.room_id
            JOIN Appointments a ON a.appointment_id = ra.appointment_id
            WHERE r.branch_id = b.branch_id
              AND r.deleted = 0
              AND a.status IN ('Completed','Scheduled')
              AND (
                    (@filter_type = 'DAILY'
                        AND ra.assignment_start >= CAST(GETDATE() AS DATE)
                        AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE))
                    )
                 OR (@filter_type = 'WEEKLY'
                        AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0)
                        AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0)
                    )
                 OR (@filter_type = 'MONTHLY'
                        AND MONTH(ra.assignment_start) = MONTH(GETDATE())
                        AND YEAR(ra.assignment_start) = YEAR(GETDATE())
                    )
              )
        ) AS [Active Rooms],

        -- Inactive Rooms
        (
            SELECT COUNT(*)
            FROM Rooms r
            WHERE r.branch_id = b.branch_id
              AND r.deleted = 0
              AND r.room_id NOT IN (
                    SELECT DISTINCT ra.room_id
                    FROM Room_Assignments ra
                    JOIN Appointments a ON a.appointment_id = ra.appointment_id
                    WHERE a.status IN ('Completed','Scheduled')
                      AND (
                            (@filter_type = 'DAILY'
                                AND ra.assignment_start >= CAST(GETDATE() AS DATE)
                                AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE))
                            )
                         OR (@filter_type = 'WEEKLY'
                                AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0)
                                AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0)
                            )
                         OR (@filter_type = 'MONTHLY'
                                AND MONTH(ra.assignment_start) = MONTH(GETDATE())
                                AND YEAR(ra.assignment_start) = YEAR(GETDATE())
                            )
                      )
              )
        ) AS [Inactive Rooms],

        /* ===================== APPOINTMENTS ===================== */

        -- Total / Completed / Cancelled / Scheduled Appointments
        (
            SELECT COUNT(*)
            FROM Appointments a
            JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
            JOIN Doctors d ON d.doctor_id = a.doctor_id
            WHERE d.branch_id = b.branch_id
              AND (
                    (@filter_type = 'DAILY'
                        AND ra.assignment_start >= CAST(GETDATE() AS DATE)
                        AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE))
                    )
                 OR (@filter_type = 'WEEKLY'
                        AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0)
                        AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0)
                    )
                 OR (@filter_type = 'MONTHLY'
                        AND MONTH(ra.assignment_start) = MONTH(GETDATE())
                        AND YEAR(ra.assignment_start) = YEAR(GETDATE())
                    )
              )
        ) AS [Total Appointments],

        -- Completed Appointments
        (
            SELECT COUNT(*)
            FROM Appointments a
            JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
            JOIN Doctors d ON d.doctor_id = a.doctor_id
            WHERE d.branch_id = b.branch_id
              AND a.status = 'Completed'
              AND (
                    (@filter_type = 'DAILY'
                        AND ra.assignment_start >= CAST(GETDATE() AS DATE)
                        AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE))
                    )
                 OR (@filter_type = 'WEEKLY'
                        AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0)
                        AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0)
                    )
                 OR (@filter_type = 'MONTHLY'
                        AND MONTH(ra.assignment_start) = MONTH(GETDATE())
                        AND YEAR(ra.assignment_start) = YEAR(GETDATE())
                    )
              )
        ) AS [Completed Appointments],

        -- Cancelled Appointments
        (
            SELECT COUNT(*)
            FROM Appointments a
            JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
            JOIN Doctors d ON d.doctor_id = a.doctor_id
            WHERE d.branch_id = b.branch_id
              AND a.status = 'Cancelled'
              AND (
                    (@filter_type = 'DAILY'
                        AND ra.assignment_start >= CAST(GETDATE() AS DATE)
                        AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE))
                    )
                 OR (@filter_type = 'WEEKLY'
                        AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0)
                        AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0)
                    )
                 OR (@filter_type = 'MONTHLY'
                        AND MONTH(ra.assignment_start) = MONTH(GETDATE())
                        AND YEAR(ra.assignment_start) = YEAR(GETDATE())
                    )
              )
        ) AS [Cancelled Appointments],

        -- Scheduled Appointments
        (
            SELECT COUNT(*)
            FROM Appointments a
            JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
            JOIN Doctors d ON d.doctor_id = a.doctor_id
            WHERE d.branch_id = b.branch_id
              AND a.status = 'Scheduled'
              AND (
                    (@filter_type = 'DAILY'
                        AND ra.assignment_start >= CAST(GETDATE() AS DATE)
                        AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE))
                    )
                 OR (@filter_type = 'WEEKLY'
                        AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0)
                        AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0)
                    )
                 OR (@filter_type = 'MONTHLY'
                        AND MONTH(ra.assignment_start) = MONTH(GETDATE())
                        AND YEAR(ra.assignment_start) = YEAR(GETDATE())
                    )
              )
        ) AS [Scheduled Appointments]

    FROM Branches b
    WHERE b.deleted = 0
    ORDER BY b.branch_id;
END;


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[GetDoctorAppointments]    Script Date: 1/14/2026 7:23:11 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER   PROCEDURE [dbo].[GetDoctorAppointments]
    @doctor_id INT,                      
    @patient_cnic VARCHAR(13) = NULL,    
    @status VARCHAR(20) = NULL          
AS
BEGIN
    SET NOCOUNT ON;

    SELECT 
        A.appointment_id,
        P.first_name + ' ' + P.last_name AS patient_name,
        P.cnic AS patient_cnic,
        A.status,
        RA.room_id,
        FORMAT(RA.assignment_start, 'yyyy-MM-dd hh:mm tt') AS assignment_start,
        FORMAT(RA.assignment_end, 'yyyy-MM-dd hh:mm tt') AS assignment_end
    FROM Appointments A
    JOIN Patients P ON A.patient_id = P.patient_id
    JOIN Room_Assignments RA ON A.appointment_id = RA.appointment_id
    WHERE 
        A.doctor_id = @doctor_id
        AND (@patient_cnic IS NULL OR P.cnic LIKE @patient_cnic + '%')
        AND (@status IS NULL OR A.status = @status)
    ORDER BY RA.assignment_start;
END


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[GetDoctorLevelReport]    Script Date: 1/14/2026 7:23:18 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER   PROCEDURE [dbo].[GetDoctorLevelReport]
    @filter_type VARCHAR(10)  -- DAILY | WEEKLY | MONTHLY
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        d.doctor_id AS [Doctor ID],
        d.cnic AS [Doctor CNIC],
        d.first_name AS [First Name],
        d.last_name As [Last Name],
        b.branch_name AS [Doctor Branch],

        /* Total Appointments for this doctor */
        (
            SELECT COUNT(*)
            FROM Appointments a
            JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
            WHERE a.doctor_id = d.doctor_id
              AND (
                    (@filter_type = 'DAILY'
                        AND ra.assignment_start >= CAST(GETDATE() AS DATE)
                        AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE))
                    )
                 OR (@filter_type = 'WEEKLY'
                        AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0)
                        AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0)
                    )
                 OR (@filter_type = 'MONTHLY'
                        AND MONTH(ra.assignment_start) = MONTH(GETDATE())
                        AND YEAR(ra.assignment_start) = YEAR(GETDATE())
                    )
              )
        ) AS [Total Appointments],

        /* Completed Appointments */
        (
            SELECT COUNT(*)
            FROM Appointments a
            JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
            WHERE a.doctor_id = d.doctor_id
              AND a.status = 'Completed'
              AND (
                    (@filter_type = 'DAILY'
                        AND ra.assignment_start >= CAST(GETDATE() AS DATE)
                        AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE))
                    )
                 OR (@filter_type = 'WEEKLY'
                        AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0)
                        AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0)
                    )
                 OR (@filter_type = 'MONTHLY'
                        AND MONTH(ra.assignment_start) = MONTH(GETDATE())
                        AND YEAR(ra.assignment_start) = YEAR(GETDATE())
                    )
              )
        ) AS [Completed Appointments],

        /* Cancelled Appointments */
        (
            SELECT COUNT(*)
            FROM Appointments a
            JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
            WHERE a.doctor_id = d.doctor_id
              AND a.status = 'Cancelled'
              AND (
                    (@filter_type = 'DAILY'
                        AND ra.assignment_start >= CAST(GETDATE() AS DATE)
                        AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE))
                    )
                 OR (@filter_type = 'WEEKLY'
                        AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0)
                        AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0)
                    )
                 OR (@filter_type = 'MONTHLY'
                        AND MONTH(ra.assignment_start) = MONTH(GETDATE())
                        AND YEAR(ra.assignment_start) = YEAR(GETDATE())
                    )
              )
        ) AS [Cancelled Appointments],

        /* Scheduled Appointments */
        (
            SELECT COUNT(*)
            FROM Appointments a
            JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
            WHERE a.doctor_id = d.doctor_id
              AND a.status = 'Scheduled'
              AND (
                    (@filter_type = 'DAILY'
                        AND ra.assignment_start >= CAST(GETDATE() AS DATE)
                        AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE))
                    )
                 OR (@filter_type = 'WEEKLY'
                        AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0)
                        AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0)
                    )
                 OR (@filter_type = 'MONTHLY'
                        AND MONTH(ra.assignment_start) = MONTH(GETDATE())
                        AND YEAR(ra.assignment_start) = YEAR(GETDATE())
                    )
              )
        ) AS [Scheduled Appointments]

    FROM Doctors d
    JOIN Branches b ON b.branch_id = d.branch_id
    WHERE d.deleted = 0
    ORDER BY d.first_name;
END;


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[GetDoctors]    Script Date: 1/14/2026 7:23:26 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[GetDoctors]
    @CNICFilter VARCHAR(33) = NULL
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        d.doctor_id,
        d.branch_id,
        b.branch_name,
        d.first_name,
        d.last_name,
        d.email,
        d.cnic,
        d.password,
        d.specialty,
        d.contact_number,
        d.created_at,
        CASE WHEN d.deleted = 1 THEN 'YES' ELSE 'NO' END AS deleted
    FROM Doctors d
    INNER JOIN Branches b ON d.branch_id = b.branch_id
    WHERE (@CNICFilter IS NULL OR d.cnic LIKE '%' + @CNICFilter + '%')
    ORDER BY d.created_at DESC
END


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[GetPatientLevelReport]    Script Date: 1/14/2026 7:23:33 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER   PROCEDURE [dbo].[GetPatientLevelReport]
    @filter_type VARCHAR(10)  -- DAILY | WEEKLY | MONTHLY
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        p.patient_id AS [Patient ID],
        p.cnic AS [Patient CNIC],
        p.first_name AS [First Name],
        p.last_name AS [Last Name],

        /* Total Appointments */
        (
            SELECT COUNT(*)
            FROM Appointments a
            JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
            WHERE a.patient_id = p.patient_id
              AND (
                    (@filter_type = 'DAILY' AND ra.assignment_start >= CAST(GETDATE() AS DATE) AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE)))
                 OR (@filter_type = 'WEEKLY' AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0) AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0))
                 OR (@filter_type = 'MONTHLY' AND MONTH(ra.assignment_start) = MONTH(GETDATE()) AND YEAR(ra.assignment_start) = YEAR(GETDATE()))
              )
        ) AS [Total Appointments],

        /* Completed Appointments */
        (
            SELECT COUNT(*)
            FROM Appointments a
            JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
            WHERE a.patient_id = p.patient_id
              AND a.status = 'Completed'
              AND (
                    (@filter_type = 'DAILY' AND ra.assignment_start >= CAST(GETDATE() AS DATE) AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE)))
                 OR (@filter_type = 'WEEKLY' AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0) AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0))
                 OR (@filter_type = 'MONTHLY' AND MONTH(ra.assignment_start) = MONTH(GETDATE()) AND YEAR(ra.assignment_start) = YEAR(GETDATE()))
              )
        ) AS [Completed Appointments],

        /* Cancelled Appointments */
        (
            SELECT COUNT(*)
            FROM Appointments a
            JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
            WHERE a.patient_id = p.patient_id
              AND a.status = 'Cancelled'
              AND (
                    (@filter_type = 'DAILY' AND ra.assignment_start >= CAST(GETDATE() AS DATE) AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE)))
                 OR (@filter_type = 'WEEKLY' AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0) AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0))
                 OR (@filter_type = 'MONTHLY' AND MONTH(ra.assignment_start) = MONTH(GETDATE()) AND YEAR(ra.assignment_start) = YEAR(GETDATE()))
              )
        ) AS [Cancelled Appointments],

        /* Scheduled Appointments */
        (
            SELECT COUNT(*)
            FROM Appointments a
            JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
            WHERE a.patient_id = p.patient_id
              AND a.status = 'Scheduled'
              AND (
                    (@filter_type = 'DAILY' AND ra.assignment_start >= CAST(GETDATE() AS DATE) AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE)))
                 OR (@filter_type = 'WEEKLY' AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0) AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0))
                 OR (@filter_type = 'MONTHLY' AND MONTH(ra.assignment_start) = MONTH(GETDATE()) AND YEAR(ra.assignment_start) = YEAR(GETDATE()))
              )
        ) AS [Scheduled Appointments],


        /* Mostly Treated By Doctor Name */
        (
            SELECT TOP 1 d.first_name + ' ' + d.last_name
            FROM (
                SELECT d2.cnic, COUNT(*) AS cnt
                FROM Appointments a
                JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
                JOIN Doctors d2 ON d2.doctor_id = a.doctor_id
                WHERE a.patient_id = p.patient_id
                  AND (
                        (@filter_type = 'DAILY' AND ra.assignment_start >= CAST(GETDATE() AS DATE) AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE)))
                     OR (@filter_type = 'WEEKLY' AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0) AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0))
                     OR (@filter_type = 'MONTHLY' AND MONTH(ra.assignment_start) = MONTH(GETDATE()) AND YEAR(ra.assignment_start) = YEAR(GETDATE()))
                  )
                GROUP BY d2.cnic
            ) AS sub
            JOIN Doctors d ON d.cnic = sub.cnic
            ORDER BY sub.cnt DESC
        ) AS [Mostly Treated By Doctor],


        /* Mostly Treated By Doctor CNIC */
        (
            SELECT TOP 1 sub.cnic
            FROM (
                SELECT d2.cnic, COUNT(*) AS cnt
                FROM Appointments a
                JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
                JOIN Doctors d2 ON d2.doctor_id = a.doctor_id
                WHERE a.patient_id = p.patient_id
                  AND (
                        (@filter_type = 'DAILY' AND ra.assignment_start >= CAST(GETDATE() AS DATE) AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE)))
                     OR (@filter_type = 'WEEKLY' AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0) AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0))
                     OR (@filter_type = 'MONTHLY' AND MONTH(ra.assignment_start) = MONTH(GETDATE()) AND YEAR(ra.assignment_start) = YEAR(GETDATE()))
                  )
                GROUP BY d2.cnic
            ) AS sub
            ORDER BY sub.cnt DESC
        ) AS [Doctor CNIC]

        

    FROM Patients p
    WHERE p.deleted = 0
    ORDER BY p.patient_id;
END;


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[GetPatients]    Script Date: 1/14/2026 7:23:49 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[GetPatients]
    @CNICFilter VARCHAR(13) = NULL
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        p.patient_id,
        p.first_name,
        p.last_name,
        p.email,
        p.cnic,
        p.password,
        p.gender,
        p.contact_number,
        p.created_at,
        CASE WHEN p.deleted = 1 THEN 'YES' ELSE 'NO' END AS deleted
    FROM Patients p
    WHERE (@CNICFilter IS NULL OR p.cnic LIKE '%' + @CNICFilter + '%')
    ORDER BY p.created_at DESC
END


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[GetRoomLevelReport]    Script Date: 1/14/2026 7:23:55 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER   PROCEDURE [dbo].[GetRoomLevelReport]
    @filter_type VARCHAR(10)   -- DAILY | WEEKLY | MONTHLY
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        r.room_id AS [Room ID],
        b.branch_name AS [Branch Name],

        /* Active Doctors in this room */
        (
            SELECT COUNT(DISTINCT d.doctor_id)
            FROM Appointments a
            JOIN Doctors d ON d.doctor_id = a.doctor_id
            JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
            WHERE ra.room_id = r.room_id
              AND a.status IN ('Completed','Scheduled')
              AND (
                    (@filter_type = 'DAILY'
                        AND ra.assignment_start >= CAST(GETDATE() AS DATE)
                        AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE))
                    )
                 OR (@filter_type = 'WEEKLY'
                        AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0)
                        AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0)
                    )
                 OR (@filter_type = 'MONTHLY'
                        AND MONTH(ra.assignment_start) = MONTH(GETDATE())
                        AND YEAR(ra.assignment_start) = YEAR(GETDATE())
                    )
              )
        ) AS [Active Doctors],

        /* Active Patients in this room */
        (
            SELECT COUNT(DISTINCT a.patient_id)
            FROM Appointments a
            JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
            WHERE ra.room_id = r.room_id
              AND a.status IN ('Completed','Scheduled')
              AND (
                    (@filter_type = 'DAILY'
                        AND ra.assignment_start >= CAST(GETDATE() AS DATE)
                        AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE))
                    )
                 OR (@filter_type = 'WEEKLY'
                        AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0)
                        AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0)
                    )
                 OR (@filter_type = 'MONTHLY'
                        AND MONTH(ra.assignment_start) = MONTH(GETDATE())
                        AND YEAR(ra.assignment_start) = YEAR(GETDATE())
                    )
              )
        ) AS [Active Patients],

        /* Total Appointments in this room */
        (
            SELECT COUNT(*)
            FROM Appointments a
            JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
            WHERE ra.room_id = r.room_id
              AND (
                    (@filter_type = 'DAILY'
                        AND ra.assignment_start >= CAST(GETDATE() AS DATE)
                        AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE))
                    )
                 OR (@filter_type = 'WEEKLY'
                        AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0)
                        AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0)
                    )
                 OR (@filter_type = 'MONTHLY'
                        AND MONTH(ra.assignment_start) = MONTH(GETDATE())
                        AND YEAR(ra.assignment_start) = YEAR(GETDATE())
                    )
              )
        ) AS [Total Appointments],

        /* Completed Appointments */
        (
            SELECT COUNT(*)
            FROM Appointments a
            JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
            WHERE ra.room_id = r.room_id
              AND a.status = 'Completed'
              AND (
                    (@filter_type = 'DAILY'
                        AND ra.assignment_start >= CAST(GETDATE() AS DATE)
                        AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE))
                    )
                 OR (@filter_type = 'WEEKLY'
                        AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0)
                        AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0)
                    )
                 OR (@filter_type = 'MONTHLY'
                        AND MONTH(ra.assignment_start) = MONTH(GETDATE())
                        AND YEAR(ra.assignment_start) = YEAR(GETDATE())
                    )
              )
        ) AS [Completed Appointments],

        /* Cancelled Appointments */
        (
            SELECT COUNT(*)
            FROM Appointments a
            JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
            WHERE ra.room_id = r.room_id
              AND a.status = 'Cancelled'
              AND (
                    (@filter_type = 'DAILY'
                        AND ra.assignment_start >= CAST(GETDATE() AS DATE)
                        AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE))
                    )
                 OR (@filter_type = 'WEEKLY'
                        AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0)
                        AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0)
                    )
                 OR (@filter_type = 'MONTHLY'
                        AND MONTH(ra.assignment_start) = MONTH(GETDATE())
                        AND YEAR(ra.assignment_start) = YEAR(GETDATE())
                    )
              )
        ) AS [Cancelled Appointments],

        /* Scheduled Appointments */
        (
            SELECT COUNT(*)
            FROM Appointments a
            JOIN Room_Assignments ra ON ra.appointment_id = a.appointment_id
            WHERE ra.room_id = r.room_id
              AND a.status = 'Scheduled'
              AND (
                    (@filter_type = 'DAILY'
                        AND ra.assignment_start >= CAST(GETDATE() AS DATE)
                        AND ra.assignment_start < DATEADD(DAY, 1, CAST(GETDATE() AS DATE))
                    )
                 OR (@filter_type = 'WEEKLY'
                        AND ra.assignment_start >= DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()), 0)
                        AND ra.assignment_start <  DATEADD(WEEK, DATEDIFF(WEEK, 0, GETDATE()) + 1, 0)
                    )
                 OR (@filter_type = 'MONTHLY'
                        AND MONTH(ra.assignment_start) = MONTH(GETDATE())
                        AND YEAR(ra.assignment_start) = YEAR(GETDATE())
                    )
              )
        ) AS [Scheduled Appointments]

    FROM Rooms r
    JOIN Branches b ON b.branch_id = r.branch_id
    WHERE r.deleted = 0
    ORDER BY r.room_id;
END;


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[GetRooms]    Script Date: 1/14/2026 7:24:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[GetRooms]
    @branch_id INT = NULL  
AS
BEGIN
    SELECT 
        r.room_id,
        r.branch_id,
        b.branch_name,
        r.deleted
    FROM Rooms r
    INNER JOIN Branches b ON r.branch_id = b.branch_id
    WHERE (@branch_id IS NULL OR r.branch_id = @branch_id)
    ORDER BY r.room_id;
END


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[InsertAdmin]    Script Date: 1/14/2026 7:24:23 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[InsertAdmin]
    @first_name VARCHAR(100),
    @last_name VARCHAR(100),
    @cnic VARCHAR(50),
    @email VARCHAR(255),
    @password VARCHAR(255),
    @deleted BIT
AS
BEGIN
    SET NOCOUNT ON;

    -- Check duplicate CNIC or Email
    IF EXISTS (SELECT 1 FROM Admin WHERE cnic = @cnic OR email = @email)
    BEGIN
        RAISERROR('Email or CNIC already exists', 16, 1);
        RETURN;
    END

    INSERT INTO Admin (first_name, last_name, cnic, email, password, deleted)
    VALUES (@first_name, @last_name, @cnic, @email, @password, @deleted);
END


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[InsertBranch]    Script Date: 1/14/2026 7:24:29 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[InsertBranch]
    @branch_name VARCHAR(255),
    @contact_number VARCHAR(100),
    @deleted BIT
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO Branches (branch_name, contact_number, deleted)
    VALUES (@branch_name, @contact_number, @deleted);
END

USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[InsertDoctor]    Script Date: 1/14/2026 7:24:36 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[InsertDoctor]
    @FirstName VARCHAR(255),
    @LastName VARCHAR(255),
    @Email VARCHAR(255),
    @CNIC VARCHAR(13),
    @Password VARCHAR(255),
    @Specialty VARCHAR(100),
    @ContactNumber VARCHAR(50),
    @BranchID INT,
    @Deleted BIT
AS
BEGIN
    SET NOCOUNT ON;

    -- Check CNIC + Branch uniqueness
    IF EXISTS (SELECT 1 FROM Doctors WHERE CNIC = @CNIC AND Branch_ID = @BranchID)
    BEGIN
        RAISERROR('CNIC already exists in this branch.', 16, 1);
        RETURN
    END

    -- Check CNIC + Password uniqueness
    IF EXISTS (SELECT 1 FROM Doctors WHERE CNIC = @CNIC AND Password = @Password)
    BEGIN
        RAISERROR('CNIC and Password combination already exists.', 16, 1);
        RETURN
    END

    INSERT INTO Doctors
    (first_name, last_name, email, cnic, password, specialty, contact_number, branch_id, deleted, created_at)
    VALUES
    (@FirstName, @LastName, @Email, @CNIC, @Password, @Specialty, @ContactNumber, @BranchID, @Deleted, GETDATE())
END


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[InsertRoom]    Script Date: 1/14/2026 7:24:42 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[InsertRoom]
    @room_id INT,
    @branch_id INT,
    @deleted BIT
AS
BEGIN
    SET IDENTITY_INSERT Rooms ON;
    INSERT INTO Rooms (room_id, branch_id, deleted)
    VALUES (@room_id, @branch_id, @deleted);
END


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[LoginUser]    Script Date: 1/14/2026 7:24:48 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER PROCEDURE [dbo].[LoginUser]
    @CNIC VARCHAR(13),
    @Password VARCHAR(255),
    @Role VARCHAR(20)
AS
BEGIN
    SET NOCOUNT ON;

    IF @Role = 'ADMIN'
    BEGIN
        SELECT admin_id AS user_id, first_name, last_name, email, cnic, password, created_at
        FROM Admin
        WHERE cnic = @CNIC AND password = @Password AND deleted = 0;
    END
    ELSE IF @Role = 'DOCTOR'
    BEGIN
        SELECT doctor_id AS user_id, first_name, last_name, email, cnic, password, specialty, contact_number, created_at , branch_id
        FROM Doctors
        WHERE cnic = @CNIC AND password = @Password AND deleted = 0;
    END
END;


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[UpdateAdmin]    Script Date: 1/14/2026 7:24:55 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[UpdateAdmin]
    @AdminID INT,
    @FirstName VARCHAR(100),
    @LastName VARCHAR(100),
    @Email VARCHAR(255),
    @CNIC VARCHAR(50),
    @Password VARCHAR(255),
    @Deleted BIT
AS
BEGIN
    SET NOCOUNT ON;

    -- Update admin
    UPDATE Admin
    SET 
        first_name = @FirstName,
        last_name = @LastName,
        email = @Email,
        cnic = @CNIC,
        password = @Password,
        deleted = @Deleted
    WHERE admin_id = @AdminID;
END


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[UpdateAdminProfile]    Script Date: 1/14/2026 7:25:02 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[UpdateAdminProfile]
    @admin_id INT,
    @first_name NVARCHAR(100),
    @last_name NVARCHAR(100),
    @email NVARCHAR(255),
    @cnic NVARCHAR(20),
    @password NVARCHAR(255)
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE Admin
    SET 
        first_name = @first_name,
        last_name  = @last_name,
        email      = @email,
        cnic       = @cnic,
        password   = @password
    WHERE admin_id = @admin_id;
END;


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[UpdateAppointment]    Script Date: 1/14/2026 7:25:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[UpdateAppointment]
    @appointment_id INT,
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

    DECLARE @patient_id INT, @doctor_id INT;

    BEGIN TRY
        BEGIN TRANSACTION;

        -- Check if appointment exists
        IF NOT EXISTS (SELECT 1 FROM Appointments WHERE appointment_id = @appointment_id)
        BEGIN
            RAISERROR('Appointment not found.', 16, 1);
        END


        -- Validate patient
        SELECT @patient_id = patient_id
        FROM Patients
        WHERE cnic = @patient_cnic AND deleted = 0;

        IF @patient_id IS NULL
        BEGIN
            RAISERROR('Invalid patient CNIC', 16, 1);
        END

        -- Validate doctor in the given branch
        SELECT @doctor_id = doctor_id
        FROM Doctors
        WHERE cnic = @doctor_cnic AND branch_id = @branch_id AND deleted = 0;

        IF @doctor_id IS NULL
        BEGIN
            RAISERROR('Invalid doctor CNIC for this branch', 16, 1);
        END

        -- Validate room in the branch
        IF NOT EXISTS (
            SELECT 1
            FROM Rooms
            WHERE room_id = @room_id AND branch_id = @branch_id AND deleted = 0
        )
        BEGIN
            RAISERROR('Invalid or deleted room for this branch.', 16, 1);
        END


        -- NEW CHECK: start time >= current datetime
        IF @assignment_start < GETDATE()
        BEGIN
            RAISERROR('Appointment start time cannot be in the past.', 16, 1);
        END

        -- Validate assignment times
        IF @assignment_start >= @assignment_end
        BEGIN
            RAISERROR('Assignment start time must be before end time.', 16, 1);
        END

        -- Check room conflict for Scheduled appointments
        IF @status = 'Scheduled'
        BEGIN
            IF EXISTS (
                SELECT 1
                FROM Room_Assignments RA
                JOIN Appointments A ON RA.appointment_id = A.appointment_id
                WHERE RA.room_id = @room_id
                  AND A.status = 'Scheduled'
                  AND RA.appointment_id != @appointment_id
                  AND (
                        (@assignment_start >= RA.assignment_start AND @assignment_start < RA.assignment_end)
                     OR (@assignment_end > RA.assignment_start AND @assignment_end <= RA.assignment_end)
                     OR (RA.assignment_start >= @assignment_start AND RA.assignment_start < @assignment_end)
                     )
            )
            BEGIN
                RAISERROR('Room already assigned during this time.', 16, 1);
            END
        END


                -- Check doctor time conflict (only Scheduled)
        IF @status = 'Scheduled'
        BEGIN
            IF EXISTS (
                SELECT 1
                FROM Appointments A
                JOIN Room_Assignments RA
                    ON A.appointment_id = RA.appointment_id
                WHERE A.doctor_id = @doctor_id
                  AND A.status = 'Scheduled'
                  AND A.appointment_id != @appointment_id   
                  AND (
                        (@assignment_start >= RA.assignment_start AND @assignment_start < RA.assignment_end)
                     OR (@assignment_end > RA.assignment_start AND @assignment_end <= RA.assignment_end)
                     OR (RA.assignment_start >= @assignment_start AND RA.assignment_start < @assignment_end)
                  )
            )
            BEGIN
                RAISERROR('Doctor already has a scheduled appointment during this time.', 16, 1);
            END
        END


        -- Check patient time conflict (only Scheduled)
        IF @status = 'Scheduled'
        BEGIN
            IF EXISTS (
                SELECT 1
                FROM Appointments A
                JOIN Room_Assignments RA
                    ON A.appointment_id = RA.appointment_id
                WHERE A.patient_id = @patient_id
                  AND A.status = 'Scheduled'
                  AND A.appointment_id != @appointment_id   
                  AND (
                        (@assignment_start >= RA.assignment_start AND @assignment_start < RA.assignment_end)
                     OR (@assignment_end > RA.assignment_start AND @assignment_end <= RA.assignment_end)
                     OR (RA.assignment_start >= @assignment_start AND RA.assignment_start < @assignment_end)
                  )
            )
            BEGIN
                RAISERROR('Patient already has a scheduled appointment during this time.', 16, 1);
            END
        END



        -- Update appointment
        UPDATE Appointments
        SET
            patient_id = @patient_id,
            doctor_id = @doctor_id,
            status = @status
        WHERE appointment_id = @appointment_id;

        -- Update room assignment
        UPDATE Room_Assignments
        SET
            room_id = @room_id,
            assignment_start = @assignment_start,
            assignment_end = @assignment_end
        WHERE appointment_id = @appointment_id;

        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;

        DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
        RAISERROR(@ErrorMessage, 16, 1);
    END CATCH
END


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[UpdateBranch]    Script Date: 1/14/2026 7:25:15 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER PROCEDURE [dbo].[UpdateBranch]
    @branch_id INT,
    @branch_name VARCHAR(255),
    @contact_number VARCHAR(100),
    @deleted BIT
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE Branches
    SET 
        branch_name = @branch_name,
        contact_number = @contact_number,
        deleted = @deleted
    WHERE branch_id = @branch_id;
END


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[UpdateDoctor]    Script Date: 1/14/2026 7:25:23 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[UpdateDoctor]
    @DoctorID INT,
    @FirstName VARCHAR(255),
    @LastName VARCHAR(255),
    @Email VARCHAR(255),
    @CNIC VARCHAR(13),
    @Password VARCHAR(255),
    @Specialty VARCHAR(100),
    @ContactNumber VARCHAR(50),
    @BranchID INT,
    @Deleted BIT
AS
BEGIN
    SET NOCOUNT ON;

    -- Check CNIC + Branch uniqueness (excluding current doctor)
    IF EXISTS (
        SELECT 1 FROM Doctors 
        WHERE CNIC = @CNIC AND Branch_ID = @BranchID AND Doctor_ID <> @DoctorID
    )
    BEGIN
        RAISERROR('CNIC already exists in this branch.', 16, 1);
        RETURN
    END

    -- Check CNIC + Password uniqueness (excluding current doctor)
    IF EXISTS (
        SELECT 1 FROM Doctors 
        WHERE CNIC = @CNIC AND Password = @Password AND Doctor_ID <> @DoctorID
    )
    BEGIN
        RAISERROR('password cannot be assigned try different password', 16, 1);
        RETURN
    END

    DECLARE @CurrentBranchID INT;

    SELECT @CurrentBranchID = branch_id 
    FROM Doctors 
    WHERE doctor_id = @DoctorID;

    -- If branch is changing
    IF @CurrentBranchID <> @BranchID
    BEGIN
        -- Check if doctor has ANY appointments
        IF EXISTS (SELECT 1 FROM Appointments WHERE doctor_id = @DoctorID)
        BEGIN
            RAISERROR('Doctor cannot be moved to another branch because appointments exist.', 16, 1);
            RETURN;
        END
    END


    UPDATE Doctors
    SET
        first_name = @FirstName,
        last_name = @LastName,
        email = @Email,
        cnic = @CNIC,
        password = @Password,
        specialty = @Specialty,
        contact_number = @ContactNumber,
        branch_id = @BranchID,
        deleted = @Deleted
    WHERE doctor_id = @DoctorID
END

USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[UpdateDoctorProfile]    Script Date: 1/14/2026 7:25:31 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[UpdateDoctorProfile]
    @doctor_id INT,
    @first_name VARCHAR(255),
    @last_name VARCHAR(255),
    @email VARCHAR(255),
    @cnic VARCHAR(13),
    @password VARCHAR(255),
    @specialty VARCHAR(100),
    @contact_number VARCHAR(50)
AS
BEGIN

    DECLARE @branch_id INT;

    -- Get doctor's branch
    SELECT @branch_id = branch_id 
    FROM Doctors 
    WHERE doctor_id = @doctor_id;

    --------------------------------------------
    -- CHECK CNIC + BRANCH UNIQUE (EXCLUDING SELF)
    --------------------------------------------
    IF EXISTS (
        SELECT 1 FROM Doctors
        WHERE cnic = @cnic
          AND branch_id = @branch_id
          AND doctor_id <> @doctor_id
    )
    BEGIN
        RAISERROR ('CNIC already exists in this branch.', 16, 1);
        RETURN;
    END

    --------------------------------------------
    -- CHECK CNIC + PASSWORD UNIQUE (EXCLUDING SELF)
    --------------------------------------------
    IF EXISTS (
        SELECT 1 FROM Doctors
        WHERE cnic = @cnic
          AND password = @password
          AND doctor_id <> @doctor_id
    )
    BEGIN
        RAISERROR ('Password cannot be assigned. Try a different password.', 16, 1);
        RETURN;
    END

    --------------------------------------------
    -- UPDATE DOCTOR
    --------------------------------------------
    UPDATE Doctors
    SET 
        first_name = @first_name,
        last_name = @last_name,
        email = @email,
        cnic = @cnic,
        password = @password,
        specialty = @specialty,
        contact_number = @contact_number
    WHERE doctor_id = @doctor_id;

END;


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[UpdatePatient]    Script Date: 1/14/2026 7:25:39 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[UpdatePatient]
    @patient_id INT,
    @first_name VARCHAR(255),
    @last_name VARCHAR(255),
    @email VARCHAR(255),
    @cnic VARCHAR(13),
    @password VARCHAR(255),
    @gender VARCHAR(50),
    @contact_number VARCHAR(50),
    @deleted BIT
AS
BEGIN
    SET NOCOUNT ON;

    -- Check CNIC duplicate (other patients only)
    IF EXISTS (SELECT 1 FROM Patients 
               WHERE cnic = @cnic AND patient_id <> @patient_id AND deleted = 0)
    BEGIN
        THROW 50001, 'CNIC already exists for another patient.', 1;
        RETURN;
    END

    -- Check Email duplicate (ignore null, other patients only)
    IF @email IS NOT NULL AND EXISTS (
        SELECT 1 FROM Patients 
        WHERE email = @email AND patient_id <> @patient_id AND deleted = 0
    )
    BEGIN
        THROW 50002, 'Email already exists for another patient.', 1;
        RETURN;
    END

    -- Update patient record
    UPDATE Patients
    SET first_name = @first_name,
        last_name = @last_name,
        email = @email,
        cnic = @cnic,
        password = @password,
        gender = @gender,
        contact_number = @contact_number,
        deleted = @deleted
    WHERE patient_id = @patient_id;
END


USE [HospitalManagementSystem]
GO
/****** Object:  StoredProcedure [dbo].[UpdateRoom]    Script Date: 1/14/2026 7:25:47 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[UpdateRoom]
    @room_id INT,         -- Room to update
    @branch_id INT,       -- New branch
    @deleted BIT          -- New deleted status
AS
BEGIN
    -- Update the room

    DECLARE @CurrentBranchID INT;

    SELECT @CurrentBranchID = branch_id
    FROM Rooms
    WHERE room_id = @room_id;

    IF @CurrentBranchID <> @branch_id
    BEGIN
        IF EXISTS (SELECT 1 FROM Room_Assignments WHERE room_id = @room_id)
        BEGIN
            RAISERROR('Room cannot be moved to another branch because it is assigned to appointments.', 16, 1);
            RETURN;
        END
    END


    UPDATE Rooms
    SET 
        branch_id = @branch_id,
        deleted = @deleted
    WHERE room_id = @room_id;
END
