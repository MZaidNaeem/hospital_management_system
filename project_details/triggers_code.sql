alter TRIGGER trg_DoctorDelete
ON Doctors
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    -- Only act when 'deleted' column is updated to 1
    UPDATE a
    SET a.status = 'Cancelled'
    FROM Appointments a
    INNER JOIN inserted i ON a.doctor_id = i.doctor_id
    INNER JOIN deleted d ON d.doctor_id = i.doctor_id
    WHERE i.deleted = 1 AND d.deleted = 0   
      AND a.status = 'Scheduled';
END;



alter TRIGGER trg_PatientDelete
ON Patients
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    -- Only act when 'deleted' column is updated to 1
    UPDATE a
    SET a.status = 'Cancelled'
    FROM Appointments a
    INNER JOIN inserted i ON a.patient_id = i.patient_id
    INNER JOIN deleted d ON d.patient_id = i.patient_id
    WHERE i.deleted = 1 AND d.deleted = 0   -- Only if it changed from 0 to 1
      AND a.status = 'Scheduled';
END;




alter TRIGGER trg_RoomDelete
ON Rooms
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    -- Cancel pending appointments for rooms just marked as deleted
    UPDATE a
    SET a.status = 'Cancelled'
    FROM Appointments a
    INNER JOIN Room_Assignments ra ON a.appointment_id = ra.appointment_id
    INNER JOIN inserted i ON ra.room_id = i.room_id
    INNER JOIN deleted d ON ra.room_id = d.room_id
    WHERE i.deleted = 1        -- room is now deleted
      AND d.deleted = 0        -- room was not deleted before
      AND a.status = 'Scheduled'; -- only pending appointments
END;