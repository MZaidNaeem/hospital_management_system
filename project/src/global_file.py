
class global_value():
    current_user = None
    current_user_window = None
    def __init__(self):
        pass
        

    @staticmethod
    def fetch_branches():
        """
        Fetches all branches from the database.
        Returns:
            branch_dict: {branch_name: branch_id}
        """
        from connection import get_connection  # import here to avoid circular import
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT branch_id, branch_name FROM Branches ORDER BY branch_name")
        rows = cursor.fetchall()
        conn.close()
        branch_dict = {branch_name: branch_id for branch_id, branch_name in rows}
        print(branch_dict)
        return branch_dict
    
    @staticmethod
    def throw_exception(e):
        full_msg = str(e)

        if "]" in full_msg:
            clean_msg = full_msg.split("]")[-1].strip()  
        else:
            clean_msg = full_msg

        return clean_msg



