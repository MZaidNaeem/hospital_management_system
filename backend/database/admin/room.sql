create PROCEDURE GetRooms
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
GO



CREATE PROCEDURE InsertRoom
    @room_id INT,
    @branch_id INT,
    @deleted BIT
AS
BEGIN
    SET IDENTITY_INSERT Rooms ON;
    INSERT INTO Rooms (room_id, branch_id, deleted)
    VALUES (@room_id, @branch_id, @deleted);
END
GO


CREATE PROCEDURE UpdateRoom
    @room_id INT,         -- Room to update
    @branch_id INT,       -- New branch
    @deleted BIT          -- New deleted status
AS
BEGIN
    -- Update the room
    UPDATE Rooms
    SET 
        branch_id = @branch_id,
        deleted = @deleted
    WHERE room_id = @room_id;
END
GO
