import sqlite3
def creat_db():
    con = sqlite3.connect(database=r'C:\Users\ACER\PycharmProjects\quanlyvattu\ims.db')
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE if not exists employee 
                    (ID INT PRIMARY KEY,
                    Ten TEXT,
                    Sdt INT,
                    GT TEXT,
                    diachi TEXT,
                    Email TEXT,
                    Luong TEXT,
                    Usertype TEXT,
                    pass TEXT)''')
    con.commit()

creat_db()