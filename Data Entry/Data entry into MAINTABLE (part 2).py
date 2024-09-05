import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='*****',database='TRAVEL_AND_TOURISM')
mycursor=mydb.cursor( )

A="insert into maintable values('France','Europe','France, country of northwestern Europe is historically and culturally among the most important nations in the Western world. France has 37 sites inscribed in the World Heritage List and features cities or sites of high cultural interest, beaches and seaside resorts, ski resorts, and rural regions that many enjoy for their beauty and tranquillity. For more than two decades, France has reigned as the worlds most popular tourist destination, receiving 82 million foreign tourists annual. People from all over the world are drawn to Frances sophisticated culture, dazzling landmarks, exquisite cuisine, fine wines, romantic chateaux and picturesque countryside.');"
mycursor.execute(A)
mydb.commit( )

B="insert into maintable values('China','Asia','China, officially the Peoples Republic of China (PRC), is a gateway to East Asia. It is the worlds most populous country, with a population of around 1.4 billion in 2019. China is one of the leading nations in the world, maintained by its large, industrious population and abundant natural resources. The depth and complexity of the Chinese civilization, with its rich heritage, has fascinated travelers such as Marco Polo in centuries past, and will continue to excite and bewilder the tourist today.');"
mycursor.execute(B)
mydb.commit( )

C="insert into maintable values('Italy','Europe','Located in Southern Europe, this boot-shaped country is one of the worlds most popular travel destinations for a number of reasons that include art treasures, trendy fashion, stunning landscapes, passionate people and top-class cuisine. Italians are known for their zeal for life, and this trait shows up in every aspect of their culture from their animated language to their superb fashion and impeccable cuisine. The country is home to the greatest number of UNESCO World Heritage Sites in the world. Exercised across the country is the Italian tradition, la passeggiata, where locals go out for an evening stroll to enjoy life as well as to show off new clothes and new romances.');"
mycursor.execute(C)
mydb.commit( )

D="insert into maintable values('Spain','Europe','Spain, officially the Kingdom of Spain, is a country in Southwestern Europe with some pockets of territory across the Strait of Gibraltar and the Atlantic Ocean.Spain is the largest country in Southern Europe. Splendid beaches, delicious cuisine, vibrant nightlife and lively fiestas all make Spain one of Europes best getaways. Because Spain encompasses several autonomous regions and islands, the country boasts one of the most widely diverse cultures and landscapes on the continent. It would be impossible to see all of Spains marvelous attractions during one vacation, so tourists are recommended to pick one region as a base and explore popular sites by day trips.');"
mycursor.execute(D)
mydb.commit( )

E="insert into maintable values('USA','North America','The United States of America is a country primarily located in central North America, between Canada and Mexico. Considering the United States is 3.8 million square miles, nearly as big as all of Europe, its easy to see why its the third-most-popular travel destination on Earth. The countrys mix of wildly diverse attractions dont hurt either, including some of the most iconic cities in the world (New York City, LA, Chicago) and a thriving national-park system.');"
mycursor.execute(E)
mydb.commit( )
