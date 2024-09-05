import mysql.connector
# create table 'COUNTRYCITY'
mydb=mysql.connector.connect(host='localhost',user='root',password='*****',database='TRAVEL_AND_TOURISM')
mycursor=mydb.cursor( )
a="create table COUNTRYCITY(COUNTRY VARCHAR(20),CITY VARCHAR(20),DESCRIPTION varchar (2000))"
mycursor.execute(a)
mydb.commit( )

# Create table 'COUNTRYTOURISM'
b="create table COUNTRYTOURISM(COUNTRY VARCHAR(20),PLACES varchar(200))"
mycursor.execute(b)
mydb.commit( )

