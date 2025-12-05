CREATE PROCEDURE GetBranches
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
GO


CREATE PROCEDURE InsertBranch
    @branch_name VARCHAR(255),
    @contact_number VARCHAR(100),
    @deleted BIT
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO Branches (branch_name, contact_number, deleted)
    VALUES (@branch_name, @contact_number, @deleted);
END
GO



CREATE PROCEDURE UpdateBranch
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
GO