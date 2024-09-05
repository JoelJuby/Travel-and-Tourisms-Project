import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='*****',database='TRAVEL_AND_TOURISM')
mycursor=mydb.cursor( )

a1="United Kingdom"
a2="London"
a3="London is the capital and largest city of England and the United Kingdom. The city stands on the River Thames in the south-east of England, at the head of its 50-mile (80 km) estuary leading to the North Sea. London has been a major settlement for two millennia. More than half of those who arrive to the UK head to London, famous for its seamless blend of history and modern urbanity (not to mention its exemplary, scot-free museums)."
A="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
a=(a1,a2,a3)
mycursor.execute(A,a)
mydb.commit( )

a4="United Kingdom"
a5="Northern Ireland"
a6="Located in the northeast of the island of Ireland, Northern Ireland is variously described as a country, province, or region, which is part of the United Kingdom.The centerpiece of Northern Ireland's geography is Lough Neagh, at 151 square miles (391 km2) the largest freshwater lake both on the island of Ireland and in the British Isles.The centerpiece of Northern Ireland's geography is Lough Neagh, at 151 square miles (391 km2) the largest freshwater lake both on the island of Ireland and in the British Isles.The vast majority of Northern Ireland has a temperate maritime climate, rather wetter in the west than the east, although cloud cover is very common across the region. The weather is unpredictable at all times of the year even though the seasons are distinct."
Q="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
q=(a4,a5,a6)
mycursor.execute(Q,q)
mydb.commit( )

a7="United Kingdom"
a8="Scotland"
a9="Covering the northern third of the island of Great Britain, mainland Scotland has a 96-mile (154 km) border with England to the southeast and is otherwise surrounded by the Atlantic Ocean to the north and west, the North Sea to the northeast and the Irish Sea to the south.The Kingdom of Scotland emerged as an independent sovereign state in the European Early Middle Ages and continued to exist until 1707, at which point it merged with England to form the United Kingdom. The climate of most of Scotland is temperate and oceanic, and tends to be very changeable."
W="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
w=(a7,a8,a9)
mycursor.execute(W,w)
mydb.commit( )

a10="United Kingdom"
a11="Wales"
a12="Wales is the least visited of the countries — just 2 percent of travelers make it here. It is bordered by England to the east, the Irish Sea to the north and west, and the Bristol Channel to the south. Wales has over 1,680 miles (2,700 km) of coastline and is largely mountainous with its higher peaks in the north and central areas, including Snowdon (Yr Wyddfa), its highest summit. The country lies within the north temperate zone and has a changeable, maritime climate."
G="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
g=(a10,a11,a12)
mycursor.execute(G,g)
mydb.commit( )

a13="United Kingdom"
a14="Edinburgh"
a15="Recognized as the capital of Scotland since at least the 15th century, Edinburgh is the seat of the Scottish Government, the Scottish Parliament and the supreme courts of Scotland. The city's Palace of Holyrood house is the official residence of the monarch in Scotland.. Edinburgh's Old Town and New Town together are listed as a UNESCO World Heritage site, which has been managed by Edinburgh World Heritage since 1999."
U="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
u=(a13,a14,a15)
mycursor.execute(U,u)
mydb.commit( )

a16="United Kingdom"
a17="Glasgow"
a18="Glasgow is situated on the River Clyde in the country's West Central Lowlands. It is the fifth most visited city in the UK. Glasgow was the 'Second City of the British Empire' for much of the Victorian era and Edwardian period, having taken the mantle from pre-independence Dublin, which was largely recognized the second city during the Georgian era although many other cities argue the title was theirs, not Glasgow's. Despite its northerly latitude, similar to that of Moscow, Glasgow's climate is classified as oceanic."
T="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
t=(a16,a17,a18)
mycursor.execute(T,t)
mydb.commit( )

b1="Thailand"
b2="Bangkok"
b3="Bangkok is the capital and most populous city of Thailand. It is known in Thai as Krung Thep Maha Nakhon or simply Krung Thep.. Bangkok traces its roots to a small trading post during the Ayutthaya Kingdom in the 15th century, which eventually grew and became the site of two capital cities: Thonburi in 1768 and Rattanakosin in 1782.It experiences three seasons: hot, rainy, and cool, although temperatures are fairly hot year-round."
Y="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
y=(b1,b2,b3)
mycursor.execute(Y,y)
mydb.commit( )

b4="Thailand"
b5="Phuket"
b6="Phuket is one of the southern provinces (changwat) of Thailand. It consists of the island of Phuket, the country's largest island, and another 32 smaller islands off its coast. It lies off the west coast of Thailand in the Andaman Sea.Phuket Province has an area of 576 km2.Phuket features a tropical monsoon climate. Due to its proximity to the equator, in the year, there is a little variation in temperatures."
I="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
i=(b4,b5,b6)
mycursor.execute(I,i)
mydb.commit( )

b7="Thailand"
b8="Krabi"
b9="Krabi is the main town in the province of Krabi (thesaban mueang) on the west coast of southern Thailand at the mouth of the Krabi River where it empties in Phang Nga Bay. Krabi is 783 km south of Bangkok by road. Facing the Andaman Sea, like Phuket, Krabi has a tropical monsoon climate, and is subject to a ten-month rainy season between March and December, often with sustained heavy rains for days at a time during the monsoons."
R="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
r=(b7,b8,b9)
mycursor.execute(R,r)
mydb.commit( )

b10="Thailand"
b11="Ko Hong Island"
b12="Hong (Room Island) is a limestone island, completely surrounded by cliff walls so that it looks like a huge hall with one entrance and open to the sky.Entering the sunlit hall from the dark cave will instill an immense feeling of the creative power of nature. When entering this natural wonder in solitude this unique experience will remain in your soul for the rest of your life.Entering the sunlit hall from the dark cave will instill an immense feeling of the creative power of nature. When entering this natural wonder in solitude this unique experience will remain in your soul for the rest of your life."
O="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
o=(b10,b11,b12)
mycursor.execute(O,o)
mydb.commit( )

b13="Thailand"
b14="Chiang Mai"
b15="Chiangmai, is the largest city in northern Thailand and the capital of Chiang Mai Province. It is 700 km (435 mi) north of Bangkok near most of the highest mountains in the country (because it is located near the Himalayas). Chiang Mai has a tropical savanna climate tempered by the low latitude and moderate elevation, with warm to hot weather year-round, though nighttime conditions during the dry season can be cool and much lower than daytime highs."
P="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
p=(b13,b14,b15)
mycursor.execute(P,p)
mydb.commit( )

b16="Thailand"
b17="Pattaya City"
b18="Pattaya City is on the east coast of the Gulf of Thailand, about 100 kilometers (62 mi) southeast of Bangkok, within, but not part of, Bang Lamung District in the province of Chonburi. Pattaya has a tropical wet and dry climate, which is divided into the following seasons: hot and dry (December to February), hot and humid (March and April), and hot and rainy (May to November)."
S="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
s=(b16,b17,b18)
mycursor.execute(S,s)
mydb.commit( )

c1="Germany"
c2="Berlin"
c3="Berlin is the capital and largest city of Germany by both area and population. Berlin is in northeastern Germany, in an area of low-lying marshy woodlands with a mainly flat topography, part of the vast Northern European Plain which stretches all the way from northern France to western Russia. Berlin has an oceanic climate the eastern part of the city has a slight continental influence, especially in the 0 °C isotherm, one of the changes being the annual rainfall according to the air masses and the greater abundance during a period of the year. This type of climate features moderate summer temperatures but sometimes hot (for being semi continental) and cold winters but not rigorous most of the time."
F="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
f=(c1,c2,c3)
mycursor.execute(F,f)
mydb.commit( )

c4="Germany"
c5="Bavaria"
c6="Bavaria is the largest German state by land area comprising roughly a fifth of the total land area of Germany. The history of Bavaria includes its earliest settlement by Iron Age Celtic tribes, followed by the conquests of the Roman Empire in the 1st century BC, when the territory was incorporated into the provinces of Raetia and Noricum..Bavaria has a unique culture, largely because of the state's large Catholic plurality and conservative traditions."
H="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
h=(c4,c5,c6)
mycursor.execute(H,h)
mydb.commit( )

c7="Germany"
c8="Ruhr"
c9="The Ruhr also referred to as Ruhr area, Ruhr district, Ruhr region, or Ruhr valley, is a polycentric urban area in North Rhine-Westphalia, Germany.The Ruhr has an oceanic climate in spite of its inland position, with mildening winds from the Atlantic travelling over the lowlands to moderate temperature extremes, in spite of its relatively northerly latitude that sees significant variety in daylight hours."
J="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
j=(c7,c8,c9)
mycursor.execute(J,j)
mydb.commit( )

c10="Germany"
c11="Northern Germany"
c12="The five coastal states (Schleswig-Holstein, Mecklenburg-Vorpommern, Lower Saxony and the two city-states Hamburg and Bremen) are regularly referred to as Northern Germany. The key terrain feature of Northern Germany is the North German Plain including the marshes along the coastline of the North and Baltic Seas, as well as the geest and heaths inland. Also prominent are the low hills of the Baltic Uplands, the ground moraines, end moraines, sandur, glacial valleys, and bogs."
Z="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
z=(c10,c11,c12)
mycursor.execute(Z,z)
mydb.commit( )

c13="Germany"
c14="Munich"
c15="Munich it is the third-largest city in Germany, after Berlin and Hamburg, and thus the largest which does not constitute its own state. Munich lies on the elevated plains of Upper Bavaria, about 50 km (31 miles) north of the northern edge of the Alps, at an altitude of about 520 m (1,706 ft) . The local rivers are the Isar and the Würm. Munich is situated in the Northern Alpine Foreland. the climate is oceanic independent of the isotherm but with some humid continental  features like warm to hot summers and cold winters, but without permanent snow cover."
K="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
k=(c13,c14,c15)
mycursor.execute(K,k)
mydb.commit( )

c16="Germany"
c17="Hamburg"
c18="One of Germany's 16 federal states, Hamburg is surrounded by Schleswig-Holstein to the north and Lower Saxony to the south. Hamburg lies on the River Elbe and two of its tributaries, the River Alster and the River Bille.Hamburg has an oceanic climate, influenced by its proximity to the coast and maritime influences that originate over the Atlantic Ocean."
L="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
l=(c16,c17,c18)
mycursor.execute(L,l)
mydb.commit( )

d1="Mexico"
d2="Mexico City"
d3="Mexico City is one of the most important cultural and financial centers in the world. It is located in the Valley of Mexico (Valle de México), a large valley in the high plateaus in the center of Mexico, at an altitude of 2,240 meters (7,350 ft).Mexico City has a subtropical highland climate, due to its tropical location but high elevation."
X="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
x=(d1,d2,d3)
mycursor.execute(X,x)
mydb.commit( )

d4="Mexico"
d5="Cancún"
d6="Cancún is a city in southeast Mexico on the northeast coast of the Yucatán Peninsula in the Mexican state of Quintana Roo. It is a significant tourist destination in Mexico and the seat of the municipality of Benito Juárez. The city is on the Caribbean Sea and is one of Mexico's easternmost points.Cancún has a tropical climate, specifically a tropical wet and dry climate, with little difference between seasons, but pronounced rainy and dry seasons. The city is hot year-round, and moderated by onshore trade winds."
V="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
v=(d4,d5,d6)
mycursor.execute(V,v)
mydb.commit( )

d7="Mexico"
d8="Chichén Itzá"
d9="Chichen Itza was a large pre-Columbian city built by the Maya people of the Terminal Classic period. The archaeological site is located in Tinúm Municipality, Yucatán State, Mexico. The site exhibits a multitude of architectural styles, reminiscent of styles seen in central Mexico and of the Puuc and Chenes styles of the Northern Maya lowlands. The presence of central Mexican styles was once thought to have been representative of direct migration or even conquest from central Mexico, but most contemporary interpretations view the presence of these non-Maya styles more as the result of cultural diffusion."
N="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
n=(d7,d8,d9)
mycursor.execute(N,n)
mydb.commit( )

d10="Mexico"
d11="Tulum"
d12="Tulum is the site of a pre-Columbian Mayan walled city which served as a major port for trade, in the Mexican state of Quintana Roo. The ruins are situated on 12-meter (39 ft) tall cliffs along the east coast of the Yucatán Peninsula on the Caribbean Sea in the state of Quintana Roo, Mexico. Tulum was one of the last cities built and inhabited by the Maya; it was at its height between the 13th and 15th centuries and managed to survive about 70 years after the Spanish began occupying Mexico. Tulum a tropical savanna climate typically with a pronounced dry season."
M="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
m=(d10,d11,d12)
mycursor.execute(M,m)
mydb.commit( )

d13="Mexico"
d14="Rosarito"
d15="Often mistakenly called Rosarito Beach because of the well-known Rosarito Beach Hotel, the town of Rosarito is one part of the municipality named Playas de Rosarito ('Beaches of Rosarito'). Its beaches and dance clubs are a popular destination for young people from the United States during the Memorial Day and Labor Day weekends. Rosarito Beaches has a semi-arid climate with Mediterranean-like precipitation patterns."
B="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
b=(d13,d14,d15)
mycursor.execute(B,b)
mydb.commit( )

d16="Mexico"
d17="Cuernavaca"
d18="Cuernavaca is the capital and largest city of the state of Morelos in Mexico. The city is located around a 90 min drive south of Mexico City using the Federal Highway 95D.Cuernavaca has long been a favorite escape for Mexico City and foreign visitors because of its warm, stable climate and abundant vegetation. The city was nicknamed the 'City of Eternal Spring' by Alexander von Humboldt in the 19th century" 
C="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
c=(d16,d17,d18)
mycursor.execute(C,c)
mydb.commit( )

e1="Turkey"
e2="Istanbul"
e3="Formerly known as Byzantium and Constantinople, Istanbul is the most populous city in Turkey and the country's economic, cultural and historic center.Istanbul is in north-western Turkey within the Marmara Region on a total area of 5,343 square kilometers (2,063 sq mi). Istanbul has a borderline Mediterranean climate, humid subtropical climate and oceanic climate, due to its location in a transitional climatic zone."
D="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
d=(e1,e2,e3)
mycursor.execute(D,d)
mydb.commit( )

e4="Turkey"
e5="Adana"
e6="Adana is a Cilician city in southern Turkey. The city is situated on the Seyhan river, 35 km (22 mi) inland from the north-eastern coast of the Mediterranean Sea.This large stretch of flat, fertile land lies southeast of the Taurus Mountains. Winters in Adana are mild and wet. Frost does occasionally occur at night almost every winter, but snow is a very rare phenomenon. Summers are long, hot, humid and dry."
Query="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
Record=(e4,e5,e6)
mycursor.execute(Query,Record)
mydb.commit( )

e7="Turkey"
e8="Antalya"
e9="Located on Anatolia's southwest coast bordered by the Taurus Mountains, Antalya is the largest Turkish city on the Mediterranean coast outside the Aegean region with over one million people in its metropolitan area.. The area is shielded from the northerly winds by the Taurus Mountains. Antalya has a hot-summer Mediterranean climate with hot and dry summers and mild and rainy winters." 
query="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
record=(e7,e8,e9)
mycursor.execute(query,record)
mydb.commit( )

e10="Turkey"
e11="Burdur"
e12="Burdur is in the 'lakes district' of Turkey and is an important habitat for birds and bird migration routes. Burdur has a hot summer Mediterranean climate with continental influences, with cold, wet and often snowy winters and very hot, long and dry summers."
Command="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
Rec=(e10,e11,e12)
mycursor.execute(Command,Rec)
mydb.commit( )

e13="Turkey"
e14="Ankara"
e15="Ankara is the capital of Turkey.The city is very old with various Hattian, Hittite, Lydian, Phrygian, Galatian, Greek, Persian, Roman, Byzantine, and Ottoman archaeological sites. The historical center of Ankara is a rocky hill rising 150 m (500 ft) over the left bank of the Ankara River, a tributary of the Sakarya River. The hill remains crowned by the ruins of Ankara Castle."
command="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
rec=(e13,e14,e15)
mycursor.execute(command,rec)
mydb.commit( )

e16="Turkey"
e17="Dalyan"
e18="Dalyan is a town in  Muğla Province located between the well-known district of Marmaris and Fethiye on the south-west coast of Turkey. Life in Dalyan revolves around the Dalyan Çayı River which flows past the town. The boats that ply up and down the river, navigating the maze of reeds, are the preferred means of transport to all the local sites."
Instruction="insert into COUNTRYCITY(COUNTRY,CITY,DESCRIPTION) values (%s,%s,%s)"
Data=(e16,e17,e18)
mycursor.execute(Instruction,Data)
mydb.commit( )













