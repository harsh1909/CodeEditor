# INTEGER TEXT NUMERIC REAL
import sqlite3


def init_db():
    conn = sqlite3.connect('databasev1.db')
    print("Opened database successfully")   
    #return 
    with conn:
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS CODESHARE 
            (

            code_id  TEXT    NOT NULL PRIMARY KEY,
            source  TEXT    );''')

        print("Table created successfully")
	    


def exist_in_db(code_id):
    conn = sqlite3.connect('databasev1.db')

    with conn:
        cur = conn.cursor()
        r = cur.execute('''SELECT * from CODESHARE where code_id = ? ''',(code_id,)).fetchone()
        print("search from db",r)
        if r:
            return True

    return False  


def create_entry_in_db(code_id):
    conn = sqlite3.connect('databasev1.db')
    print("hello form database create entry")
    with conn:
        cur = conn.cursor()
        cur.execute('''INSERT INTO CODESHARE(
        code_id,source
        )
        VALUES(?,?)''',[code_id,""])

        conn.commit()
		
def submit_data(data):
    conn = sqlite3.connect('databasev1.db')
    print("hello form database submit")
    with conn:
        cur = conn.cursor()
        cur.execute('''UPDATE CODESHARE
                       SET source = ?
                       WHERE code_id = ?''',data[::-1])

        conn.commit()    


def fetch_source_code(code_id):
    print("code id = ",code_id)
    conn = sqlite3.connect('databasev1.db')

    with conn:
        cur = conn.cursor()
        r = cur.execute('''SELECT * from CODESHARE where code_id = ? ''',(code_id,)).fetchone()
        print("results from db",r)

    if r:
        return r[1]
    
    return ""

