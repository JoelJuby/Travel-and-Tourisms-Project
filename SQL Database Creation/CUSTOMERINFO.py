import mysql.connector
# create table 'CUSTOMERINFO'
mydb=mysql.connector.connect(host='localhost',user='root',password='*****',database='TRAVEL_AND_TOURISM')
mycursor=mydb.cursor( )
f="create table CUSTOMERINFO(MOBILE varchar(20),EMAIL varchar(60),ID varchar (8),NAME varchar(30),STATUS varchar(15))"
mycursor.execute(f)
mydb.commit( )
