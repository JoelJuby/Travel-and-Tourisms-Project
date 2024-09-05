import mysql.connector
# create table 'FARES'
mydb=mysql.connector.connect(host='localhost',user='root',password='*****',database='TRAVEL_AND_TOURISM')
mycursor=mydb.cursor( )
d="create table FARES(COUNTRY varchar(20),AIRFARE INT(5),HOTELFARE INT(5),CURRENCYNAME varchar(20))"
mycursor.execute(d)
mydb.commit( )
