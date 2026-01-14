import pyodbc

server = 'DESKTOP-G4IVL0P'
database = 'HospitalManagementSystem'
username = ''  
password = '' 

# Windows Authentication
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'


def get_connection():
    """
    Establishes and returns a connection to the SQL Server database
    """
    try:
        conn = pyodbc.connect(connection_string)
        print("✓ Successfully connected to SQL Server database!")
        return conn
    except pyodbc.Error as e:
        print(f"✗ Error connecting to database: {e}")
        return None
    


def test_connection():
    """
    Tests the database connection and retrieves data from Admin table
    """
    conn = get_connection()
    
    if conn:
        try:
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM Admin ")
            admins = cursor.fetchall()
            
            print("\n--- Admin Table Data ---")
            for admin in admins:
                for col in admin:
                    print(col)
            
            cursor.close()
            
        except pyodbc.Error as e:
            print(f"✗ Error executing query: {e}")




# test_connection()
# get_connection()
