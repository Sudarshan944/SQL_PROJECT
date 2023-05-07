import mysql.connector
mydb = mysql.connector.connect(
    host='localhost', user='root', password='8500659446', database='INVENTORY_MANAGEMENT')
cur = mydb.cursor()
# Update the manufacture details of all the red-colored toys which are purchased by the “MyKids” store.
q2 = 'UPDATE MANUFACTURE SET NUMBER_ITEMS=10 WHERE PRODUCT_NAME="TOY CAR" AND COLOR="RED"'
cur.execute(q2)
print("Updated Successfully")