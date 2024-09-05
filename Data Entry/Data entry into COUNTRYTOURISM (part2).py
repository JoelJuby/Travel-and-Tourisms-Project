import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="*****",database="TRAVEL_AND_TOURISM")
mycursor=mydb.cursor()

A1="insert into countrytourism values('France','Eiffel Tower,Paris');"
mycursor.execute(A1)
mydb.commit( )
A2="insert into countrytourism values('France','Louvre,Paris');"
mycursor.execute(A2)
mydb.commit( )
A3="insert into countrytourism values('France','Notre Dame de Paris,Paris');"
mycursor.execute(A3)
mydb.commit( )
A4="insert into countrytourism values('France','Palace of Versailles,Versailless');"
mycursor.execute(A4)
mydb.commit( )
A5="insert into countrytourism values('France','Villa Savoye,Poissy');"
mycursor.execute(A5)
mydb.commit( )
A6="insert into countrytourism values('France','Museum of Port Royal des Champs,Yvelines');"
mycursor.execute(A6)
mydb.commit( )

B1="insert into countrytourism values('China','Great Wall of China,Huairou District');"
mycursor.execute(B1)
mydb.commit( )
B2="insert into countrytourism values('China','Forbidden City,Beijing');"
mycursor.execute(B2)
mydb.commit( )
B3="insert into countrytourism values('China','Victoria Harbour,Hong Kong');"
mycursor.execute(B3)
mydb.commit( )
B4="insert into countrytourism values('China','Terracotta Army,Xian');"
mycursor.execute(B4)
mydb.commit( )
B5="insert into countrytourism values('China','Pudong Skyline,Shanghai');"
mycursor.execute(B5)
mydb.commit( )
B6="insert into countrytourism values('China','Hani Terraces,Yunnan');"
mycursor.execute(B6)
mydb.commit( )

C1="insert into countrytourism values('Italy','Colosseum in Rome,Rome');"
mycursor.execute(C1)
mydb.commit( )
C2="insert into countrytourism values('Italy','Grand Canal in Venice,Venice');"
mycursor.execute(C2)
mydb.commit( )
C3="insert into countrytourism values('Italy','Santa Maria del Fiore in Florence,Florence');"
mycursor.execute(C3)
mydb.commit( )
C4="insert into countrytourism values('Italy','Pompeii,Naples');"
mycursor.execute(C4)
mydb.commit( )
C5="insert into countrytourism values('Italy','Leaning Tower of Pisa,Pisa');"
mycursor.execute(C5)
mydb.commit( )
C6="insert into countrytourism values('Italy','Santa Maria delle Grazie in Milan,Milan');"
mycursor.execute(C6)
mydb.commit( )
 
D1="insert into countrytourism values('Spain','Alhambra,Granada');"
mycursor.execute(D1)
mydb.commit( )
D2="insert into countrytourism values('Spain','Mezquita of Cordoba');"
mycursor.execute(D2)
mydb.commit( )
D3="insert into countrytourism values('Spain','El Escorial,Madrid');"
mycursor.execute(D3)
mydb.commit( )
D4="insert into countrytourism values('Spain','Sagrada Familia,Barcelona');"
mycursor.execute(D4)
mydb.commit( )
D5="insert into countrytourism values('Spain','Ibiza,Balearic Sea');"
mycursor.execute(D5)
mydb.commit( )
D6="insert into countrytourism values('Spain','Aqueduct of Segovia,Segovia');"
mycursor.execute(D6)
mydb.commit( )
 
E1="insert into countrytourism values('USA','Grand Canyon,Arizona');"
mycursor.execute(E1)
mydb.commit( )
E2="insert into countrytourism values('USA','Golden Gate Bridge,San Francisco');"
mycursor.execute(E2)
mydb.commit( )
E3="insert into countrytourism values('USA','Niagara Falls,New York');"
mycursor.execute(E3)
mydb.commit( )
E4="insert into countrytourism values('USA','Las Vegas Strip,Nevada');"
mycursor.execute(E4)
mydb.commit( )
E5="insert into countrytourism values('USA','Walt Disney World in Orlando,Orlando');"
mycursor.execute(E5)
mydb.commit( )
E6="insert into countrytourism values('USA','Navy Pier,Chicago');"
mycursor.execute(E6)
mydb.commit( ) 





