import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mu97@woR',

    )

cursorObject = database.cursor()

cursorObject.execute('create database mydatabase')

print("All Done")