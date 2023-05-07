import mysql.connector
mydb = mysql.connector.connect(
    host='localhost', user='root', password='8500659446', database='INVENTORY_MANAGEMENT')
cur = mydb.cursor()
# Display all the “wooden chair” items that were manufactured before the 1st May 2023.
q3 = 'SELECT * FROM MANUFACTURE WHERE PRODUCT_NAME="WOODEN CHAIR" AND MANUFACTURE_DATE < "2023-05-01"'
cur.execute(q3)
display1 = cur.fetchall()
for x in display1:
    print(x)
