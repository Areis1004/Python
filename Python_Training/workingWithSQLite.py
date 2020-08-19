import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(r"D:\SQLite\db\employees.db") 
        print("Connected To Database")
    except Error as err:
        print(err.args[0]   )
    return conn

def create_table():
    conn = create_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS empListData (
                id integer PRIMARY_KEY,
                name text NOT NULL,
                avatar text,
                createdAt text
            );
        """)
    except Error as err:
        print(err)
    finally:
        if conn: conn.close()

def insertValue():
    create_table()
    conn = create_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO empListData (id, name, avatar, createdAt)
            VALUES
            (11, "Mayank", "", ""),
            (2, "Anshul", "", ""),
            (3, "Ankit", "", "");
        """)
        conn.commit()
    except Error as err:
        print(err.args[0])
    finally:
        conn.close()

def select_data():
    conn = create_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM empListData")
        rows = cur.fetchall()
        for data in rows:
            print(data)
    except Error as err:
        print(err)

def delete_data():
    conn = create_connection()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM empListData where id=1")
        conn.commit()
    except Error as err:
        print(err.args[0])
    finally:
        if conn:
            conn.close()


def update_data():
    conn = create_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
            UPDATE empListData SET name = "Anshul" where id = 1
        """)
        conn.commit()
    except Error as err:
        print(err)
    finally:
        conn.close()

insertValue()
select_data()
