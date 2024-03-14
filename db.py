import sqlite3

def create_db():
    con = sqlite3.connect(database=r'db.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(empID INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,email TEXT,gender TEXT ,contact TEXT,dob TEXT,doj TEXT,pass TEXT,utype TEXT ,address TEXT,salary TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,contact TEXT,desc TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(catID INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product(proID INTEGER PRIMARY KEY AUTOINCREMENT,Category TEXT,Supplier TEXT,Name TEXT ,price TEXT,qty TEXT,status TEXT)")
    con.commit()

create_db()