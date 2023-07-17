import mysql.connector

conn = mysql.connector.connect(username='root', password='Sg@83192003',host='localhost',database='sys',port=3306)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()