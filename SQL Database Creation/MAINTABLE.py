import mysql.connector
# create table 'MAINTABLE'
mydb=mysql.connector.connect(host='localhost',user='root',password='*****',database='TRAVEL_AND_TOURISM')
mycursor=mydb.cursor( )
a="create table MAINTABLE(COUNTRY varchar(20),CONTINENT varchar(20),DESCRIPTION varchar (2000))"
mycursor.execute(a)
mydb.commit( )
