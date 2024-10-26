# Install mysql on your computer
# pip install mysql
# pip install mysql-connector
# OR
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

# prepare a cursor object
curssorObject = dataBase.cursor()

# Create a dataBase
curssorObject.execute("CREATE DATABASE elderco")
