import mysql.connector

cnx = mysql.connector.connect(user='root', password='', host='localhost', database='testapp')

cursor = cnx.cursor()


cursor.execute("SELECT * FROM products")


rows = cursor.fetchall()


for row in rows:
    print(row[1])

cursor.close()
cnx.close()


