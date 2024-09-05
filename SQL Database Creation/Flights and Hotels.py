import mysql.connector
# create table 'FLIGHTS'
mydb=mysql.connector.connect(host='localhost',user='root',password='*****',database='TRAVEL_AND_TOURISM')
mycursor=mydb.cursor( )
a="create table FLIGHTS(SLNO VARCHAR(2),FLIGHTNAME VARCHAR(20),ECONMULT decimal(2,1),BUSINESSMULT decimal(2,1))"
mycursor.execute(a)
mydb.commit( )

# Create table 'HOTELS'
b="create table HOTELS(SLNO VARCHAR(2),NAME varchar(20),MULTIPLIER decimal(2,1))"
mycursor.execute(b)
mydb.commit( )
