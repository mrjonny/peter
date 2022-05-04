import sqlite3

con=sqlite3.connect("employee.db")
print("database created succesfully")

con.execute("create table EMPLOYEE (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,email TEXT UNIQUE NOT NULL,address TEXT NOT NULL)")
print("table created succesfully")

con.close()