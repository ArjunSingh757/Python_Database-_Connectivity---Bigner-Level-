import mysql.connector as a
from mysql.connector import Error
conn=a.connect(host="localhost",user="root",password="root",database="place_tre")
if conn.is_connected():
    print("Succes")
else:
    print("fail")

mycu=conn.cursor()
mycu.execute("alter table customer add column id int auto_increment primary key")
mycu.execute("show tables")
print("tables")
for c in mycu:
    print(c)