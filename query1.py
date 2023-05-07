import mysql.connector
mydb = mysql.connector.connect(
    host='localhost', user='root', password='8500659446', database='INVENTORY_MANAGEMENT')
cur = mydb.cursor()
# Delete the defective item, e.g., the shirt which was accidentally purchased by the “ORay” store, manufactured on the date ‘01-04-23’.
q1 = 'DELETE FROM MANUFACTURE WHERE DEFECTIVE=1'
cur.execute(q1)
print("Deleted Successfully")