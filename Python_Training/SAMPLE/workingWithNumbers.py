import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

#create_connection(r"D:\SQLite\db\employees.db")

create_projects_table_sql = """ CREATE TABLE IF NOT EXISTS empList (
                            id integer PRIMARY KEY,
                            name text NOT NULL,
                            avatar text,
                            createdAt text
                        ); """

def create_table(db_file, create_table_sql):
    conn = sqlite3.connect(db_file)
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

#create_table(r"D:\SQLite\db\employees.db", create_projects_table_sql)

def create_employee():
    conn = sqlite3.connect(r"D:\SQLite\db\employees.db")
    sql = ''' INSERT INTO empList(id,name, avatar, createdAt)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (4, "Mayank", "No Avatar", "Today"))
    conn.commit()
    return cur.lastrowid

#create_employee()

def select_all_tasks():
    conn = sqlite3.connect(r"D:\SQLite\db\employees.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM empList")

    rows = cur.fetchall()

    for row in rows:
        print(row)

#select_all_tasks()

def delete_task():
    conn = sqlite3.connect(r"D:\SQLite\db\employees.db")
    sql = 'DELETE FROM empList WHERE id=2'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

delete_task()

select_all_tasks()

def update_task():
    conn = sqlite3.connect(r"D:\SQLite\db\employees.db")
    sql = ''' UPDATE empList
              SET name = ? 
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, ("Anshul", 1))
    conn.commit()

#update_task()

#select_all_tasks()

#create_employee()

#sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS empList (
#                                    id integer PRIMARY KEY,
#                                    name text NOT NULL,
#                                    avatar text,
#                                    createdAt text
#                                ); """
#
#create_table(r"D:\SQLite\db\employees.db", sql_create_projects_table)