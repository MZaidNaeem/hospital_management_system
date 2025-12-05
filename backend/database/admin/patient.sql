CREATE PROCEDURE AddPatient
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
GO




CREATE PROCEDURE AddPatient
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
GO








CREATE PROCEDURE UpdatePatient
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
GO