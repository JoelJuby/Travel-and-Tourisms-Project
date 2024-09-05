import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='*****',database='TRAVEL_AND_TOURISM')
mycursor=mydb.cursor( )

A="insert into maintable values ('Russia','Asia','Where to begin in this country spanning an extraordinary 6.6 million square miles? Moscow and St. Petersburg are of course excellent places to start, though you would also be wise to explore overlooked gems like the ancient town of Sezdal.');"
mycursor.execute(A)
mydb.commit( )

B="insert into maintable values ('Portugal','Europe','Portugal is a southern European country on the Iberian Peninsula, bordering Spain. Its location on the Atlantic Ocean has influenced many aspects of its culture: salt cod and grilled sardines are national dishes, and the beaches are a major tourist destination.');"
mycursor.execute(B)
mydb.commit( )

C="insert into maintable values ('Malaysia','Asia','Malaysia is a small country with 13 states in South East Asia. It is located between Singapore in the South and Thailand on the North. The capital city is Kuala Lumpur. The highest mountain in South East Asia, named Mount Kinaballu is located in Malaysia.');"
mycursor.execute(C)
mydb.commit( )

D="insert into maintable values ('Canada','North America','Canada is a country in the northern part of North America. Its ten provinces and three territories extend from the Atlantic to the Pacific and northward into the Arctic Ocean, covering 9.98 million square kilometres, making it the worlds second-largest country by total area.');"
mycursor.execute(D)
mydb.commit( )

E="insert into maintable values ('Netherlands','Europe','When people think of the Netherlands, they often think of Amsterdam, home to historic canals, museums both impressive and quirky, and a thriving nightlife scene. But the Netherlands Board of Tourism and Conventions wants visitors to discover it is so much more than its capital.');"
mycursor.execute(E)
mydb.commit( )
