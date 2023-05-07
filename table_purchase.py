import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root',
                                password='8500659446', database='INVENTORY_MANAGEMENT')
cur = mydb.cursor()
t = 'CREATE TABLE PURCHASE(PURCHASE_ID INT PRIMARY KEY NOT NULL,STORE_MODE VARCHAR(40) NOT NULL,PRODUCT_NAME VARCHAR(20) NOT NULL,COLOR VARCHAR(10) NOT NULL,NUMBER_ITEMS INT NOT NULL,PURCHASE_DATE DATE NOT NULL,PURCHASE_AMOUNT FLOAT NOT NULL);'
cur.execute(t)
mydb.commit()