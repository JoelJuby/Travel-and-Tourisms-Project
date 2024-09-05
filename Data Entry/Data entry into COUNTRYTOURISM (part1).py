import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="*****",database="TRAVEL_AND_TOURISM")
mycursor=mydb.cursor()

a1="insert into COUNTRYTOURISM values('United Kingdom','Stonehenge')"
mycursor.execute(a1)
mydb.commit( )
a2="insert into COUNTRYTOURISM values('United Kingdom','Tower of London')"
mycursor.execute(a2)
mydb.commit( )
a3="insert into COUNTRYTOURISM values('United Kingdom','The British Museum')"
mycursor.execute(a3)
mydb.commit( )
a4="insert into COUNTRYTOURISM values('United Kingdom','Chester Zoo')"
mycursor.execute(a4)
mydb.commit( )
a5="insert into COUNTRYTOURISM values('United Kingdom','Eden Project')"
mycursor.execute(a5)
mydb.commit( )
a6="insert into COUNTRYTOURISM values('United Kingdom','Warwick Castle')"
mycursor.execute(a6)
mydb.commit( )

b1="insert into COUNTRYTOURISM values('Thailand','Railay Beach')"
mycursor.execute(b1)
mydb.commit( )
b2="insert into COUNTRYTOURISM values('Thailand','Koh Phi Phi')"
mycursor.execute(b2)
mydb.commit( )
b3="insert into COUNTRYTOURISM values('Thailand','The Grand Palace')"
mycursor.execute(b3)
mydb.commit( )
b4="insert into COUNTRYTOURISM values('Thailand','Khao Yai National Park')"
mycursor.execute(b4)
mydb.commit( )
b5="insert into COUNTRYTOURISM values('Thailand','Historic City of Ayutthaya')"
mycursor.execute(b5)
mydb.commit( )
b6="insert into COUNTRYTOURISM values('Thailand','Pai')"
mycursor.execute(b6)
mydb.commit( )

c1="insert into COUNTRYTOURISM values('Germany','Brandenburg Gate')"
mycursor.execute(c1)
mydb.commit( )
c2="insert into COUNTRYTOURISM values('Germany','Cologne Cathedral')"
mycursor.execute(c2)
mydb.commit( )
c3="insert into COUNTRYTOURISM values('Germany','The Black Forest')"
mycursor.execute(c3)
mydb.commit( )
c4="insert into COUNTRYTOURISM values('Germany','Neuschwanstein Castle')"
mycursor.execute(c4)
mydb.commit( )
c5="insert into COUNTRYTOURISM values('Germany','The Rhine Valley')"
mycursor.execute(c5)
mydb.commit( )
c6="insert into COUNTRYTOURISM values('Germany','Kings Island')"
mycursor.execute(c6)
mydb.commit( )

d1="insert into COUNTRYTOURISM values('Mexico','Monarch Butterfly Biosphere Reserve')"
mycursor.execute(d1)
mydb.commit( )
d2="insert into COUNTRYTOURISM values('Mexico','Great Pyramid of Cholula')"
mycursor.execute(d2)
mydb.commit( )
d3="insert into COUNTRYTOURISM values('Mexico','Uxmal')"
mycursor.execute(d3)
mydb.commit( )
d4="insert into COUNTRYTOURISM values('Mexico','Zipolite')"
mycursor.execute(d4)
mydb.commit( )
d5="insert into COUNTRYTOURISM values('Mexico','El Tajin')"
mycursor.execute(d5)
mydb.commit( )
d6="insert into COUNTRYTOURISM values('Mexico','Isla Mujeres')"
mycursor.execute(d6)
mydb.commit( )

e1="insert into COUNTRYTOURISM values('Turkey','Ephesus')"
mycursor.execute(e1)
mydb.commit( )
e2="insert into COUNTRYTOURISM values('Turkey','Cappadocia')"
mycursor.execute(e2)
mydb.commit( )
e3="insert into COUNTRYTOURISM values('Turkey','Topkapi Palace')"
mycursor.execute(e3)
mydb.commit( )
e4="insert into COUNTRYTOURISM values('Turkey','Pamukkale')"
mycursor.execute(e4)
mydb.commit( )
e5="insert into COUNTRYTOURISM values('Turkey','Sumela Monastery')"
mycursor.execute(e5)
mydb.commit( )
e6="insert into COUNTRYTOURISM values('Turkey','Mount Nemrut')"
mycursor.execute(e6)
mydb.commit( )
