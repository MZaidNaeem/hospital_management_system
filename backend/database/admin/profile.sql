---------------
--------------- LOGIN
---------------


USE HospitalManagementSystem;
GO

CREATE PROCEDURE LoginUser
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
    ELSE IF @Role = 'PATIENT'
    BEGIN
        SELECT patient_id AS user_id, first_name, last_name, email,cnic, password, gender, contact_number, created_at
        FROM Patients
        WHERE cnic = @CNIC AND password = @Password AND deleted = 0;
    END
END;
GO


DROP PROCEDURE IF EXISTS LoginUser;



EXEC LoginUser 
    @CNIC = '1', 
    @Password = '123', 
    @Role = 'ADMIN';

EXEC LoginUser 
    @CNIC = '3', 
    @Password = '123', 
    @Role = 'DOCTOR';


EXEC LoginUser 
    @CNIC = '5', 
    @Password = '123', 
    @Role = 'PATIENT';






---------------
--------------- Admin profile update and delete
---------------




CREATE PROCEDURE UpdateAdminProfile
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
GO


EXEC UpdateAdminProfile 
    @admin_id = 1, 
    @first_name = 'Zaid', 
    @last_name = 'Naeem', 
    @email = 'zaid@example.com', 
    @cnic = '1', 
    @password = '123';





CREATE PROCEDURE DeleteAdminProfile
    @admin_id INT
AS
BEGIN
    SET NOCOUNT ON;

    -- This DELETE will be intercepted by the trigger
    DELETE FROM admin
    WHERE admin_id = @admin_id;
END;
GO