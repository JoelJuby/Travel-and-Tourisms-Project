import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='*****',database='TRAVEL_AND_TOURISM')
mycursor=mydb.cursor( )

A="insert into conversion values('France',000.45,001.19,087.94);"
mycursor.execute(A)
mydb.commit( )
B="insert into conversion values('Spain',000.45,0001.19,087.94);"
mycursor.execute(B)
mydb.commit( )
C="insert into conversion values('USA',000.38,001.00,074.24);"
mycursor.execute(C)
mydb.commit( )
D="insert into conversion values('China',000.05,000.15,011.30);"
mycursor.execute(D)
mydb.commit( )
E="insert into conversion values('Italy',000.45,001.19,087.94);"
mycursor.execute(E)
mydb.commit( )
F="insert into conversion values('Turkey',000.04,000.13,009.63);"
mycursor.execute(F)
mydb.commit( )
G="insert into conversion values('Mexico',000.01,000.05,003.65);"
mycursor.execute(G)
mydb.commit( )
H="insert into conversion values('Germany',000.45,001.19,087.94);"
mycursor.execute(H)
mydb.commit( )
I="insert into conversion values('Thailand',000.01,000.03,002.45);"
mycursor.execute(I)
mydb.commit( )
J="insert into conversion values('United Kingdom',000.50,001.33,098.50);"
mycursor.execute(J)
mydb.commit( )
K="insert into conversion values('Japan',000.03,000.09,000.71);"
mycursor.execute(K)
mydb.commit( )
L="insert into conversion values('Austria',000.45,001.19,087.94);"
mycursor.execute(L)
mydb.commit( )
M="insert into conversion values('Greece',000.45,001.19,087.94);"
mycursor.execute(M)
mydb.commit( )
N="insert into conversion values('Hong Kong',000.04,000.13,009.58);"
mycursor.execute(N)
mydb.commit( )
O="insert into conversion values('Malaysia',000.09,000.24,018.16);"
mycursor.execute(O)
mydb.commit( )
