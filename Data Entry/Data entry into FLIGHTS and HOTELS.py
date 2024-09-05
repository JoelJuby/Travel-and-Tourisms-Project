import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='*****',database='TRAVEL_AND_TOURISM')
mycursor=mydb.cursor( )

# Entering the flight details
a="insert into FLIGHTS values('1','Emirates',2.3,5.0)"
mycursor.execute(a)
mydb.commit( )
b="insert into FLIGHTS values('2','Lufthansa',1.3,2.4)"
mycursor.execute(b)
mydb.commit( )
c="insert into FLIGHTS values('3','Qatar Airways',2.0,4.3)"
mycursor.execute(c)
mydb.commit( )
d="insert into FLIGHTS values('4','Eva Air',1.6,3.0)"
mycursor.execute(d)
mydb.commit( )
e="insert into FLIGHTS values('5','Air India',1.2,2.3)"
mycursor.execute(e)
mydb.commit( )

# Entering the hotel details
f="insert into HOTELS values('1','Garden Inn',5.6)"
mycursor.execute(f)
mydb.commit( )
g="insert into HOTELS values('2','Hyatt Place',2.2)"
mycursor.execute(g)
mydb.commit( )
h="insert into HOTELS values('3','Courtyard',4.2)"
mycursor.execute(h)
mydb.commit( )
i="insert into HOTELS values('4','Days Inn',1.9)"
mycursor.execute(i)
mydb.commit( )
j="insert into HOTELS values('5','Hampton',3.4)"
mycursor.execute(j)
mydb.commit( )
