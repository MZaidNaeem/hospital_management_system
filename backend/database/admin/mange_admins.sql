CREATE PROCEDURE GetAdminsExceptSelf
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
              OR a.cnic = @filter_cnic
            )
    ORDER BY a.created_at DESC;
END
GO





CREATE PROCEDURE UpdateAdmin
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

    -- Check if email already exists for another admin
    IF EXISTS (
        SELECT 1 
        FROM Admin 
        WHERE email = @Email AND admin_id <> @AdminID
    )
    BEGIN
        RAISERROR ('Email already exists.', 16, 1);
        RETURN;
    END

    -- Check CNIC uniqueness
    IF EXISTS (
        SELECT 1 
        FROM Admin
        WHERE cnic = @CNIC AND admin_id <> @AdminID
    )
    BEGIN
        RAISERROR ('CNIC already exists.', 16, 1);
        RETURN;
    END

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
GO


