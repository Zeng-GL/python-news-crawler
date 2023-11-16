import pymysql

db_connect = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '54Lucas09@',
    charset = 'utf8',
    database = 'pydb'
)

with db_connect.cursor() as cursor:
    # 新增資料表
    ### 問題1: 不加int欄位，就會出現error A
    sql_cr_tb = """
    CREATE TABLE IF NOT EXISTS Member(
        ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Name varchar(20),
        Height int(6),
        Weight int(6)
    );
    """

    # 新增資料至資料表
    sql_add = """
    INSERT INTO Member (Name, Height, Weight) VALUES 
    ('Alan', 170, 78), 
    ('John', 185, 83),
    ('Momo', 183, 75)
    """

    # 更新資料
    sql_update = """
    UPDATE Member SET Height=180 WHERE Name='John'
    """
    # cursor.execute(sql_update)
    # db_connect.commit()

    # 查詢全部資料
    sql_query_all = """
    SELECT * from Member
    """
    # 查詢部分資料
    sql_query_part= """
    SELECT * FROM Member WHERE Name='John'
    """

    # 刪除資料
    sq_del = """
    DELETE FROM Member WHERE Name='John'
    """
    cursor.execute(sq_del)
    db_connect.commit()

    # 執行 SQL 指令
    cursor.execute(sql_query_part)

     # 取出全部資料
    all_data = cursor.fetchall()
    print(all_data)
    # 取出第一筆資料
    first_data = cursor.fetchone()

    # 提交至 SQL
    db_connect.commit()
# 關閉 SQL 連線
db_connect.close()