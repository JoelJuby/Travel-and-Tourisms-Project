import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="*****",database="TRAVEL_AND_TOURISM")
mycursor=mydb.cursor()

A1="insert into countrycity values('France','Paris','With some of the most recognizable buildings and monuments in the world, Paris is a must-see city to visit. From the stunning art collections at the Louvre to the eerie catacombs beneath the streets and the breath taking Notre-Dame Cathedral, you could spend a lifetime getting to know all of Paris´ wonderful sights.');"
mycursor.execute(A1)
mydb.commit( )

A2="insert into countrycity values('France','Bordeaux','Straddling the banks of the Garonne River, Bordeaux is a large city with a lot to offer. Its impressive old town is delightful to walk around, and the architecture on show is ravishing.');"
mycursor.execute(A2)
mydb.commit( )

A3="insert into countrycity values('France','Lille','The largest city in the north of France, it has a lovely city center and vibrant cultural sector, with numerous museums that are worth checking out.');"
mycursor.execute(A3)
mydb.commit( )

A4="insert into countrycity values('France','Nice','Nice is constantly bathed in sunshine. As the fifth largest city in France, it has a vibrant mix of cultures.For a great view of the city and the shimmering Mediterranean Sea below, head to the Colline du Chateau. A charming place to spend some time, Nice has something for everyone, as it combines city life with a beautiful setting.');"
mycursor.execute(A4)
mydb.commit( )

A5="insert into countrycity values('France','Lyon','An orderly and sophisticated place, renaissance buildings dot its streets. Lyon seamlessly mixes the new with the old, with a rich cultural heritage that encompasses gastronomic delights and fine architecture.');"
mycursor.execute(A5)
mydb.commit( )

A6="insert into countrycity values('France','Annecy','Lying on the shores of Lake Annecy, the city´s surroundings are stunning, and visitors can hike, bike or swim in the nearby natural attractions. With a 14th century castle located in the center, it´s a picturesque and memorable place to visit.');"
mycursor.execute(A6)
mydb.commit( )

B1="insert into countrycity values('China','Beijing','With over twenty million people residing in the nations capital, Beijing is a bustling and expansive city with a plethora of attractions for visitors to delight in. As a first stop, many head to the huge Tiananmen Square which is bordered by so many fine buildings.From Beijing, it is just under an hour to visit some of the nicest parts of the Great Wall of China.');"
mycursor.execute(B1)
mydb.commit( )

B2="insert into countrycity values('China','Shanghai','As the largest city in China, Shanghai is a thriving place with a wealth of things to see and do. Lying on the banks of Huangpu River, the towering skyscrapers make for a spectacular sight. Due to Shanghai´s rapid growth over the last century, the city is an eclectic mix of different architectural styles and as a commercial center it is great for shopping in.');"
mycursor.execute(B2)
mydb.commit( )

B3="insert into countrycity values('China','Xian','With a plethora of historical sites littered around the city, it certainly is tough to see everything in Xi´an. The Army of Terracotta Warriors and Horses however is an absolute must and they really are spellbinding to behold. Chinese civilization spread forth from this influential city and although rampant modernization has changed the face of Xi´an you can still find numerous sites that testify to its former glory.');"
mycursor.execute(B3)
mydb.commit( )

B4="insert into countrycity values('China','Lhasa','The capital of Tibet, Lhasa is a mesmerising city to visit and it is situated in a beautiful and mountainous environment in the Himalayas. The Potala Palace is the primary site of interest and the incredible building looks absolutely amazing. Very different from the rest of China; head here for an insight into the rich Tibetan culture.');"
mycursor.execute(B4)
mydb.commit( )

B5="insert into countrycity values('China','Guilin','The otherworldly scenery that is found in Giulin and its surroundings makes this an awe-inspiring place to visit. Relaxing on a boat drifting down the Li River is a magical experience as the spectacular karst features of the landscape pass by on either side of you. An incredibly beautiful city, many visitors to Guilin head to the Moon and Sun Pagoda for the lovely view it offers over the area.');"
mycursor.execute(B5)
mydb.commit( )

B6="insert into countrycity values('China','Harbin','Famed for the incredible Ice Festival that takes places in the city each year, Harbin´s location in the far north of China means that it can get very cold. Due to its proximity to Russia, there is a lot of Russian influence in terms of culture and architecture and this makes Harbin a unique place to visit.');"
mycursor.execute(B6)
mydb.commit( )

C1="insert into countrycity values('Italy','Rome','While Romes iconic landmarks – such as the Colosseum and Roman Forum – need no introduction, with over three-thousand years of history, the city is saturated with fantastic historical monuments, piazzas, churches, mansions and more for visitors to explore.');"
mycursor.execute(C1)
mydb.commit( )

C2="insert into countrycity values('Italy','Florence','The birthplace of the Renaissance, Florence is mesmerizing to walk around and its historic center is full of beautiful art and stunning architecture.Delightful cafes and restaurants look out over the ancient cobbles, and with fantastic shopping on offer, as well as sumptuous Tuscan cuisine and delicious wines, Florence will never disappoint.');"
mycursor.execute(C2)
mydb.commit( )

C3="insert into countrycity values('Italy','Venice','A simply magical city, Venice is like no other place on earth. Located in the middle of a lagoon, its beautiful canals and waterways are lined with stunning buildings, palaces and churches. The winding alleys between them lead you on to yet more delights.');"
mycursor.execute(C3)
mydb.commit( )

C4="insert into countrycity values('Italy','Naples','Lying on the Gulf of Naples, this energetic city is full of life and vigor, with a wealth of cultural and historic sites to visit. There are two royal palaces to explore, as well as three castles and numerous ruins dating back over the ages – not to mention the vast array of architectural marvels on offer.');"
mycursor.execute(C4)
mydb.commit( )

C5="insert into countrycity values('Italy','Milan','Home to numerous breathtaking art collections, the citys museums are captivating and its streets are lined with beautiful art-deco architecture, among other styles. Throughout the city, you will find fantastic dining wherever you turn; Milan has the most Michelin Star establishments in all of Italy.');"
mycursor.execute(C5)
mydb.commit( )

C6="insert into countrycity values('Italy','Pisa','Much more than just the iconic Learning Tower, the former maritime power of Pisa now relies on tourists to fuel its economy.More authentic than many Italian cities which have become inundated by tourists, Pisas prestigious university means the city has a large student population – this manifests itself in the lively atmosphere evident in its bars and cafes.');"
mycursor.execute(C6)
mydb.commit( )

D1="insert into countrycity values('Spain','Barcelona','Bathed in sunshine, the capital city of Catalunya is mesmerizing to navigate, thanks to its incredible architecture that spans the ages. Lying next to the sea, there are some great seafood restaurants to check out, as well as the citys lovely beaches with a range of water activities to enjoy.');"
mycursor.execute(D1)
mydb.commit( )

D2="insert into countrycity values('Spain','Madrid','Lying at the heart of Spain, the capital is a dynamic place brimming with life and energy which is infectious to experience. Its incredible galleries and museums are home to the best of Picasso, Dali, Goya, and more.If youre looking for some fun well into the early hours, Madrid has a thriving and lively nightlife scene.');"
mycursor.execute(D2)
mydb.commit( )

D3="insert into countrycity values('Spain','Seville','With its cavernous Gothic cathedral lying at the heart of a picturesque historic center, Seville perfectly mixes the old with the new. The capital of Andalusia has some fascinating palaces, churches and streets to explore, with the medieval Jewish quarter the area that most tourists gravitate towards.');"
mycursor.execute(D3)
mydb.commit( )

D4="insert into countrycity values('Spain','Valencia','Valencias vibrant cultural scene, hopping nightlife and fine beaches mean that theres something for everyone to enjoy.With lovely, leafy parks snaking their way along the old riverbed that cuts through its center, the old quarter is great to explore, and there are lots of interesting museums to visit and many fine dining options available.');"
mycursor.execute(D4)
mydb.commit( )

D5="insert into countrycity values('Spain','Granada','With the enchanting Alhambra set amidst such gorgeous scenery, most visitors to Granada descend upon the city to explore the breathtaking palace fortress. Its amazing gardens and lovely Islamic architecture is the undoubted highlight of what Granada has to offer. The city center itself is wonderful to get lost in, as impressive churches and atmospheric bars are interspersed among fantastic Islamic architecture.');"
mycursor.execute(D5)
mydb.commit( )

D6="insert into countrycity values('Spain','Bilbao','Bilbaos iconic Guggenheim museum is probably what the city is best known for, although it certainly has much more to offer. Leafy parks and atmospheric plazas are surrounded by world-class restaurants and atmospheric eateries, showing off the best of Basque cuisine. The city has some picturesque hills overlooking it, from which there are some stunning views of the buildings below.');"
mycursor.execute(D6)
mydb.commit( )


E1="insert into countrycity values('USA','New York City','The jewel in the crown of the USA when it comes to urban areas, New York is a megacity that is absolutely packed full of iconic places, areas, and buildings. Some of New Yorks most notable landmarks that can be toured include the Statue of Liberty, the Empire State Building and the Rockefeller Center.');"
mycursor.execute(E1)
mydb.commit( )

E2="insert into countrycity values('USA','San Francisco','Set on the tip of a peninsula, San Francisco is a beautiful city in northern California. The Golden Gate Bridge is the citys number one attraction. Tourists can drive, bike ride or walk across this famous suspension bridge to admire and photograph stunning views.');"
mycursor.execute(E2)
mydb.commit( )

E3="insert into countrycity values('USA','Las Vegas','You wouldnt think a city in the middle of the desert in Nevada would be as popular as it is, but its thanks to the cavalcade of casinos here that Las Vegas is so famous. On the main street called the Strip, there are the Bellagios impressive fountain shows, a replica of the Eiffel Tower and of an Egyptian pyramid, among other landmarks.');"
mycursor.execute(E3)
mydb.commit( )

E4="insert into countrycity values('USA','Chicago','Nicknamed the Windy City and best known for its towering skyscrapers, sports teams and unique style of hot dogs and pizzas, Chicago is the third-largest city in the USA.Chicago is a huge city with many ethnic neighborhoods and a buzzing downtown district that is quite walkable. A stroll downtown offers views of impressive skyscrapers, upscale malls, quaint shops, restaurants, bakeries and numerous hot dog stands.');"
mycursor.execute(E4)
mydb.commit( )


E5="insert into countrycity values('USA','Los Angeles','Often regarded as the Entertainment Capital of the World, LA is awash with celebrity culture. You can see the handprints of film stars on Hollywood Boulevard or go on a tour to see stars homes in Beverly Hills.');"
mycursor.execute(E5)
mydb.commit( )

E6="insert into countrycity values('USA','Washington DC','The capital of the United States and seat of the federal government, Washington is a city located on the countrys East Coast in the District of Columbia. A cosmopolitan city that is home to many diverse cultures, Washington is widely known by its many iconic landmarks like the White House, Capitol Building, the Washington Monument and the Lincoln Memorial.');"
mycursor.execute(E6)
mydb.commit( )



