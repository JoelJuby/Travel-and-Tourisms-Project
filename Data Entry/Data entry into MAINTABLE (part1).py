import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='*****',database='TRAVEL_AND_TOURISM')
mycursor=mydb.cursor( )

a1="United Kingdom"
a2="Europe"
a3="On 1 May 1707, the Kingdom of Great Britain was formed, the result of Acts of Union being passed by the parliaments of England and Scotland to ratify the 1706 Treaty of Union and so unite the two kingdoms. Now made up of four countries (England, Wales, Scotland and Northern Ireland) that all speak English, the UK has long been a beloved destination among international travelers. Though it slipped slightly between 2017 and 2018, moving from No. 7 to No. 10 on the most-visited-countries list, Visit Britain estimates a rebound this year, with tourism growing another 6 percent."
A="insert into MAINTABLE(COUNTRY,CONTINENT,DESCRIPTION) values (%s,%s,%s)"
r=(a1,a2,a3)
mycursor.execute(A,r)
mydb.commit( )

b1="Thailand"
b2="Asia"
b3="Thailand, officially the Kingdom of Thailand and formerly known as Siam, is a country in Southeast Asia. Located at the center of the Indochinese Peninsula, it is composed of 76 provinces, and covers an area of 513,120 square kilometers (198,120 sq mi), and a population of over 66 million people Thailand is the world's 50th-largest country by land area, and the 22nd-most-populous country in the world. The country welcomed nearly 3 million more tourists in 2018 than 2017 and witnessed $6 billion in spending!"
B="insert into MAINTABLE(COUNTRY,CONTINENT,DESCRIPTION) values (%s,%s,%s)"
rec=(b1,b2,b3)
mycursor.execute(B,rec)
mydb.commit( )

c1="Germany"
c2="Europe"
c3="Germany's visitor count has been steadily climbing for nine consecutive years. In 2017 and 2018, Germany even ranked 1st in the world on the Nation Brands Index for its popularity. The country is most beloved among other Europeans, particularly the Dutch. Travelers from the United States are the largest market from overseas. Both Europeans and Americans rave about the country's thought-provoking historic attractions, spirited cities, vast forests (they cover one-third of the nation!) and — most importantly — excellent beer."
C="insert into MAINTABLE(COUNTRY,CONTINENT,DESCRIPTION) values (%s,%s,%s)"
record=(c1,c2,c3)
mycursor.execute(C,record)
mydb.commit( )

d1="Mexico"
d2="North America"
d3="Mexico broke its tourism record in 2018 and took in more than $20.3 billion doing so. Postcard-perfect beaches remain a major draw here, but the country's tourism board has also successfully highlighted its ancient history, cultural institutions, diverse cuisine and natural features beyond the shoreline, including butterfly sanctuaries, canyons and waterfalls."
D="insert into MAINTABLE(COUNTRY,CONTINENT,DESCRIPTION) values (%s,%s,%s)"
R=(d1,d2,d3)
mycursor.execute(D,R)
mydb.commit( )

e1="Turkey"
e2="Europe"
e3="Turkey is a transcontinental country located mainly on the Anatolian Peninsula in Western Asia, with a smaller portion on the Balkan Peninsula in Southeastern Europe. One of the earliest permanently settled regions, present-day Turkey was home to important Neolithic sites such as Göbekli Tepe, the world's oldest known temple founded in the 10th millennium BC, and Çatalhöyük, which has evidence of early agriculture and cattle and sheep domestication.The coastal areas bordering the Black Sea have a temperate oceanic climate with warm, wet summers and cool to cold, wet winters."
E="insert into MAINTABLE(COUNTRY,CONTINENT,DESCRIPTION) values (%s,%s,%s)"
Record=(e1,e2,e3)
mycursor.execute(E,Record)
mydb.commit( )


