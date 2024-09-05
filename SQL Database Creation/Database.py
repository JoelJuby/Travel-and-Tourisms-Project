import mysql.connector
#create 'database travel_and_tourism'
mydb=mysql.connector.connect(host='localhost',user='root',password='joel2003',)
mycursor=mydb.cursor( )
mycursor.execute("create database TRAVEL_AND_TOURISM")
mydb.commit( )



