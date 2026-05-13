import pyodbc as db

class DBConnection:
    con = None
    
    @staticmethod
    def get_connection():
        
        if DBConnection.con == None:
            try:
                connection_string = """
                                    DRIVER={ODBC Driver 17 for SQL Server};
                                    SERVER=localhost\\SQLEXPRESS;
                                    DATABASE=appdb;
                                    Trusted_Connection=yes;
                                    """
                DBConnection.con = db.connect(connection_string)
                print("Database connection successful.")
            
            except:
                print("Database connection unsuccessful.")
            
        return DBConnection.con
    
    @staticmethod
    def close_connection():
        if DBConnection.con is not None:
            print("Connection closed successfully.")
            return DBConnection.con.close()
        else:
            print("Connection already closed.")
