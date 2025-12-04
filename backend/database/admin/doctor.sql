CREATE PROCEDURE GetDoctors
    @CNICFilter VARCHAR(13) = NULL
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
GO




CREATE PROCEDURE InsertDoctor
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



CREATE PROCEDURE UpdateDoctor
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
        RAISERROR('CNIC and Password combination already exists.', 16, 1);
        RETURN
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

