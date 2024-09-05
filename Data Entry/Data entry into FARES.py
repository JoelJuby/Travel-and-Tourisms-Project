import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="*****",database="TRAVEL_AND_TOURISM")
mycursor=mydb.cursor()

A="insert into fares values('United Kingdom',1000,90,'Pound');"
mycursor.execute(A)
mydb.commit( )

B="insert into fares values('Thailand',550,50,'Baht');"
mycursor.execute(B)
mydb.commit( )

C="insert into fares values('Germany',900,65,'Euro');"
mycursor.execute(C)
mydb.commit( )

D="insert into fares values('Mexico',1500,40,'Peso');"
mycursor.execute(D)
mydb.commit( )

E="insert into fares values('Turkey',1500,40,'Lira');"
mycursor.execute(E)
mydb.commit( )

F="insert into fares values('France',1250,100,'Euro');"
mycursor.execute(F)
mydb.commit( )

G="insert into fares values('China',1000,45,'Yuan');"
mycursor.execute(G)
mydb.commit( )

H="insert into fares values('Italy',950,60,'Euro');"
mycursor.execute(H)
mydb.commit( )

I="insert into fares values('Spain',870,55,'Euro');"
mycursor.execute(I)
mydb.commit( )

J="insert into fares values('USA',1100,75,'USD');"
mycursor.execute(J)
mydb.commit( ) 

