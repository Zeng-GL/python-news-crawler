import pymysql
import settings

class db_obj:
    db_connect = pymysql.connect(
    host = settings.host,
    port = settings.port,
    user = settings.user,
    passwd = settings.passwd,
    db = settings.db
    )
    def __init__(self):
        pass

    def create_table(self):
        with self.db_connect.cursor() as cursor:
            sql_cr_tb = """
                CREATE TABLE IF NOT EXISTS Linenews(
                    ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    Title varchar(100),
                    View_num int(10) 
                );
                """
            cursor.execute(sql_cr_tb)
            self.db_connect.commit()
        self.db_connect.close()
    
    def add_column(self):
        with self.db_connect.cursor() as cursor:
            sql_add_col = """
                ALTER TABLE Linenews \
                ADD Subtitle varchar(500)
                ADD Link varchar(1000)
                """
            cursor.execute(sql_add_col)
            self.db_connect.commit()
        self.db_connect.close()

    def insert_data(self,d_list):
        with self.db_connect.cursor() as cursor:
            sql_insert_data = """
            INSERT INTO Linenews (
                Title) 
                VALUES (%s)
            """
            for item in d_list:
                cursor.execute(sql_insert_data,item)
                # print(item)
    
            self.db_connect.commit()
        self.db_connect.close()


    def query_all(self):
        with self.db_connect.cursor() as cursor:
            sql_query_all = """
                SELECT * from Linenews
            """
            cursor.execute(sql_query_all)
            self.db_connect.commit()
        self.db_connect.close()
            
    def query_part(self,keyword):
        with self.db_connect.cursor() as cursor:
            sql_query_part = f"SELECT * FROM Linenews WHERE column_name = '{keyword}'"
            cursor.execute(sql_query_part)
            self.db_connect.commit()
        self.db_connect.close()
    