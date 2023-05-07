import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="8500659446")
cur = mydb.cursor()
cur.execute("CREATE DATABASE INVENTORY_MANAGEMENT")