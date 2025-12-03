# pip install mysql-connector-python 

"""
create database database_name; 

table : 
    create table table_name 
    
insert : 
    insert into table_name (column_name) values (value);
"""

"""import mysql.connector 

conn = mysql.connector.connect(
    host="localhost",
    port = 3306,
    user="root",
    password="root"
)

cursor =conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS deyaan_sql;")

print("Database created successfully")
cursor.close()
conn.close()"""