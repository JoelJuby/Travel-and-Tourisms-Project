import mysql.connector
# create table 'CONVERSION'
mydb=mysql.connector.connect(host='localhost',user='root',password='*****',database='TRAVEL_AND_TOURISM')
mycursor=mydb.cursor( )
e="create table CONVERSION(COUNTRY varchar(20),RATEBHD decimal(5,2),RATEUSD decimal(5,2),RATEINR decimal(5,2))"
mycursor.execute(e)
mydb.commit( )
