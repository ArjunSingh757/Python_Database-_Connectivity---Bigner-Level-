import mysql.connector as a
from mysql.connector import Error
conn=a.connect(host="localhost",user="root",password="root",database="place_tre")
mycu=conn.cursor()
sql="select *from customer order by name"
#sql="select * from customer order by address"
#sql="select * from customer order by address"

mycu.execute(sql)
myRe=mycu.fetchall()
for x in myRe:
    print(x)