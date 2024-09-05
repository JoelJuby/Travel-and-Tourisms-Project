import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="*****",database="TRAVEL_AND_TOURISM")
mycursor=mydb.cursor()
import random
from tabulate import tabulate

n=None
m=None
totalhotel=None
totalair=None
countryname=None

#CONSUMER FUNCTIONS#

def deco():
    #use to create line of decor
    print("><"*76)

def mainmenu():
    #use to return back to menu
    deco()
    print("\n")
    global n
    x="***WELCOME TO TEAM 2 TRAVEL AND TOURISM INC.***"
    y='ENTER 1 FOR BOOKING'
    t='ENTER 2 FOR CANCELLATION'
    z='ENTER 3 IF YOU ARE AN EMPLOYEE'
    k="ENTER 0 IN ORDER TO EXIT"
    print(x.center(158),"\n",y.center(158),"\n",t.center(156),"\n",z.center(155),"\n\n",k.center(156),end="\n\n\n")
    deco()
    n=int(input("> Kindly enter your choice :"))

def maintable():
    #use to display screen 1 for consumer
    global m
    com="select country,continent from MAINTABLE"
    mycursor.execute(com)
    lists=mycursor.fetchall()
    deco()
    print(tabulate(lists,headers=["COUNTRY","CONTINENT"],tablefmt='fancy_grid'))
    deco()    
    m=input("> Kindly enter name of country you are interested in :")

def CONSUMERSCREEN1():
    #displays the main consumer screen
     global m
     m=m.capitalize()
     print("\n",m.center(154),"\n\n")
     com="select description from MAINTABLE where country='{}'".format(m)
     mycursor.execute(com)
     lists=mycursor.fetchall()
     print("==>",lists[0][0],"\n")
     print("## Cities you are recommended to visit during your stay in {} include ## ".format(m),"\n")
     com="select city,description from COUNTRYCITY where country='{}'".format(m)
     mycursor.execute(com)
     lists=mycursor.fetchall()
     for tuples in lists:
         print("<>",tuples[0],"\n","->",tuples[1],"\n")
         
     print("## Popular tourist attractions in {} include ## ".format(m),"\n")
     com="select places from COUNTRYTOURISM where country='{}'".format(m)
     mycursor.execute(com)
     lists=mycursor.fetchall()
     for tuples in lists:
         print("<>",tuples[0])
     print("\n")
     deco()

def calculatecost():
    #used in total cost calculation
    global x
    com="select airfare,hotelfare,currencyname from FARES where country='{}'".format(m)
    mycursor.execute(com)
    lists=mycursor.fetchall()
    air=lists[0][0]
    hotel=lists[0][1]
    currency=lists[0][2]
    return air,hotel,currency

def flights():
     #used to display available flights
     global y
     global totalair
     fares=calculatecost()
     currency=fares[2]
     airfare=fares[0]
     com="select slno,flightname,econmult,businessmult from flights"
     mycursor.execute(com)
     lists=mycursor.fetchall()
     deco()
     k=0
     print("SL.NO","\t\t","AIRLINE","\t\t","ECONOMY CLASS","\t\t","BUSINESS CLASS")
     print("+"*80)
     for tuples in lists:
         print(">",tuples[0],"\t\t",tuples[1],"\t\t",airfare*tuples[2]," ",currency,"\t\t",airfare*tuples[3]," ",currency)
         k+=1
     deco()
     print("\n")
     n=input("Enter serial number of the airline of your choice :")
     print("\n")
     a=input("Enter class preference (E/B) :")
     print("\n")
     deco()
     a=a.upper()
     for tuples in lists:
         if tuples[0]==n:
             if a=="E":
                 mult=tuples[2]
             else:
                 mult=tuples[3]
     totalair=airfare*mult*y
     
def hotelsandflights():
     #used for display of both hotels and flights
     global m
     global x
     global y
     global z
     global totalhotel
     global totalair
     fares=calculatecost()
     hotelfare=fares[1]
     currency=fares[2]
     com="select slno,name,multiplier from hotels"
     mycursor.execute(com)
     lists=mycursor.fetchall()
     com="select city from countrycity where country='{}'".format(m)
     mycursor.execute(com)
     lists2=mycursor.fetchall()
     L=[]
     for tuples in lists2:
         L.append(tuples[0])
     k=0
     print("SL.NO","\t\t","HOTEL","\t\t\t","CITY","\t\t\t","PRICE/NIGHT")
     print("+"*80)
     for tuples in lists:
         print(">",tuples[0],"\t\t",tuples[1],"\t\t",L[k],"\t\t",hotelfare*tuples[2]," ",currency)
         k+=1
     deco()
     print("\n")
     n=input("> Enter serial number of the hotel of your choice :")
     for tuples in lists:
         if tuples[0]==n:
             mult=tuples[2]
             break
     totalhotel=hotelfare*mult*z*x
     print("\n")
     flights()
     print("\n")
     print("> Total flight cost (for all travellers) is :",totalair,currency,"\n")
     print("> Total hotel cost (for all travellers) is :",totalhotel,currency,"\n")
     print("> Total cost of trip for all travellers is estimated at :",totalair+totalhotel,currency)
     print("\n")

def convertor():
    #used for currency conversion
    global m
    global a
    com="select ratebhd,rateusd from CONVERSION where country='{}'".format(m)
    mycursor.execute(com)
    lists=mycursor.fetchall()
    tuples=lists[0]
    if a==1:
        currency="BHD"
        rate=tuples[0]
    elif a==2:
        currency="USD"
        rate=tuples[1]
    return rate,currency

def booking():
     #booking mechanism
     global mob
     email=input("> Enter email address :")
     print("\n")
     method=input("> Enter method of payment [CREDIT CARD/DEBIT CARD] :")
     print("\n")
     deco()
     print("\n")
     print(">>WELCOME TO EZPAY SECURE PAYMENT GATEWAY<<".center(158))
     cred=int(input("> ENTER CARD NUMBER :"))
     print("\n")
     date=input("> ENTER DATE OF EXPIRY [MM/YYYY] :")
     print("\n")
     name=input("> ENTER NAME OF CARDHOLDER :")
     print("\n")
     deco()
     print(">>EZPAY SECURE PAYMENT GATEWAY<<".center(158))
     print("> Card Number : ",cred,"\n")
     print("> Expiry Date : ",date,"\n")
     print("> Name of card holder :",name,"\n")
     global totalsir
     global totalhotel
     global currency
     global x
     global y
     global z
     global r
     
     cost=(totalair*r)+(totalhotel*r)
     print("> AMOUNT TO BE PAID : ",cost,currency,"\n")
     n=input("> Press Y to confirm payment :")
     print("\n")
     deco()
     print("\n")
     print("> CONGRATULATIONS !!!! You have successfully completed the booking of your trip !!","\n")
     ran="2002"+str(random.randint(1000,2000))
     print("> Your booking ID is : ",ran, "\n")
     print("> *DO NOT SHARE THE ABOVE BOOKING ID WITH ANYONE. KINDLY SAVE IT TO AVAIL OUR OTHER SERVICES*","\n")
     print("> Your booking confirmation shall be sent to your e-mail address within 24 hours","\n")
     print("> For more information/queries, kindly contact us at team2@gmail.com")
     print("\n")
     print("> You may also contact us at 38726382/36478283")
     print("\n\n\n","THANK YOU FOR USING OUR SERVICES, WE LOOK FORWARD TO HELPING YOU PLAN YOUR DREAM VACATION ONCE AGAIN".center(155))
     print("\n")
     com="insert into CUSTOMERINFO values('{}','{}','{}','{}','{}')".format(mob,email,ran,name,"ACTIVE")
     mycursor.execute(com)
     mydb.commit()

def cancellation():
    #used to cancel a booking
    global cancel
    com="update CUSTOMERINFO set status='CANCELLED' where ID={}".format(cancel)
    mycursor.execute(com)
    mydb.commit()



# EMPLOYEE FUNCTIONS #
def rateupdate():
    #used to change conversion rate
    print("\n")
    country=input("> Enter name of country whose conversion rates you would like to edit : ")
    print("\n")
    country=country.upper()
    L=['ratebhd','rateusd','rateinr']
    for i in range(3):
        t=L[i]
        n=input("> Would you like to edit {} (Y/N)".format(t))
        n.upper()
        if n in "Yy":
            print("\n")
            x=float(input("> Enter new conversion rate : "))
            print("\n")
            com="update conversion set {}={} where country='{}'".format(t,x,country)
            mycursor.execute(com)
            mydb.commit()

def editflightmult():
    #used to edit flight multipliers
    mycursor.execute("select SLNO,FLIGHTNAME from flights")
    result=mycursor.fetchall()
    print(tabulate(result,headers=['SLNO','FLIGHTNAME',],tablefmt='fancy_grid'))
    print("\n")
    a=input("> Enter the name of the flight whose multiplier is to be edited :")
    mycursor.execute("select * from flights where FLIGHTNAME='{}'".format(a))
    result=mycursor.fetchall( )
    print(tabulate(result,headers=['SLNO','FLIGHTNAME','ECONMULT','BUSINESSMULT'],tablefmt='fancy_grid'))
    print("\n")
    M=input('> Are you sure you wish to edit this flight ? (Y/N) : ')
    print("\n")
    if M in "Yy":
       N=input(">Which multiplier do you wish to edit ? (E/B) :")
       if N in "Ee":
          print("\n")
          X=input("> Enter new multiplier : ")
          print("\n")
          query="update flights set ECONMULT='{}' where FLIGHTNAME='{}'".format(X,a)
          mycursor.execute(query)
          mydb.commit( )
          mycursor.execute("select * from flights where FLIGHTNAME='{}'".format(a))
          result=mycursor.fetchall( )
          print(tabulate(result,headers=['SLNO','FLIGHTNAME','ECONMULT','BUSINESSMULT'],tablefmt='fancy_grid'))
       elif N in "Bb":
            print("\n")
            Y=input("> Enter new multiplier :")
            query="update flights set BUSINESSMULT='{}' where FLIGHTNAME='{}'".format(Y,a)
            mycursor.execute(query)
            mydb.commit()
            mycursor.execute("select * from flights where FLIGHTNAME='{}'".format(a))
            result=mycursor.fetchall( )
            print(tabulate(result,headers=['SLNO','FLIGHTNAME','ECONMULT','BUSINESSMULT'],tablefmt='fancy_grid'))
    elif M in 'Nn':
         print('> You may try again later')
         
def edithotelmult():
    # used to edit hotel multipliers
    mycursor.execute("select SLNO,NAME from HOTELS")
    result=mycursor.fetchall( )
    print(tabulate(result,headers=['SLNO','HOTELNAME'],tablefmt="fancy_grid"))
    print("\n")
    b=input("> Enter the name of the hotel whose multiplier is to be edited :")
    mycursor.execute("select * from hotels where NAME='{}'".format(b))
    result=mycursor.fetchall( )
    print("\n")
    print(tabulate(result,headers=['SLNO','HOTELNAME','MULTIPLIER'],tablefmt='fancy_grid'))
    X=input('> Are you sure you wish to edit this hotel ? (Y/N) : ')
    print("\n")
    if X in 'Yy':
       print("\n")
       Y=input('>Enter new multiplier :')
       print("\n")
       query="update hotels set MULTIPLIER='{}' where NAME='{}'".format(Y,b)
       mycursor.execute(query)
       mydb.commit()
       mycursor.execute("select * from hotels where NAME='{}'".format(b))
       result=mycursor.fetchall()
       print(tabulate(result,headers=['SLNO','HOTELNAME','MULTIPLIER'],tablefmt='fancy_grid'))
    elif X in 'Nn':
         print('>You may try again later')

def insertcity(identifier):
      #used to add city to countrycity table
      if identifier==1:
          global countryname
      else:
            print("\n")  
            countryname=input("> Enter name of country :")
      print("\n")
      ncity=int(input("> Enter number of cities to be added :"))
      for i in range (ncity):
           print("\n")
           m=input('> Enter name of city to be added :')
           print("\n")
           n=input('> Enter description of city :')
           print("\n")
           com="insert into COUNTRYCITY values ('{}','{}','{}')".format(countryname,m,n)
           mycursor.execute(com)
           mydb.commit()

def inserttourism(identifier): 
      #used to add a tourist place to countrytourism table
      if identifier==1:
            global countryname
      else:
            print("\n")
            countryname=input("> Enter name of country where attraction is located :")
      print("\n") 
      ntourism=int(input("> Enter number of tourist attractions to be added :"))
      for i in range (ntourism):
             print("\n")
             t=input("Enter name of tourist attraction to be added :")
             print("\n")
             com="insert into COUNTRYTOURISM values ('{}','{}')".format(countryname,t)
             mycursor.execute(com)
             mydb.commit()

def insertfares():
      #only used in insertcountry to add new fares
      global countryname
      print("\n")
      a=int(input("> Enter average airfare :"))
      print("\n")
      h=int(input("> Enter average hotelfare :"))
      print("\n")
      curry=input(">Enter currency name :")
      print("\n")
      com="insert into FARES values ('{}','{}','{}','{}')".format(countryname,a,h,curry)
      mycursor.execute(com)
      mydb.commit()


def updatefares():
      print("\n")
      c=input("> Enter name of country where base hotel/airfares are to be edited :")
      print("\n")
      h=int(input("> Enter new hotel fare :"))
      print("\n")
      a=int(input("> Enter new air fare :"))
      print("\n")
      com="update FARES set AIRFARE='{}', HOTELFARE='{}' where country='{}'".format(c,a,h)
      mycursor.execute(com)
      mydb.commit()


def insertcountry():
      #used to add new country
      global countryname
      print("\n")
      countryname=input('> Enter name of country to be inserted :')
      print("\n")
      s=input('> Enter name of continent :')
      print("\n")
      n=input('> Enter description of country :')
      print("\n")
      com="insert into MAINTABLE values ('{}','{}','{}')".format(countryname,s,n)
      mycursor.execute(com)
      mydb.commit()
      i=float(input("> Enter conversion rate to INR :"))
      b=float(input("> Enter conversion rate to BHD :"))
      d=float(input("> Enter conversion rate to USD :"))
      newcom="insert into CONVERSION values ('{}','{}','{}','{}')".format(countryname,b,d,i)
      mycursor.execute(newcom)
      mydb.commit()
      insertcity(1)
      inserttourism(1)
      insertfares()

def updatecitydesc():
     #used to edit description of city
     print("\n")
     m=input('> Enter name of city to be edited :')
     print("\n")
     s=input('> Enter new description :')
     print("\n")
     com="update COUNTRYCITY set description='{}' where city='{}'".format(s,m)
     mycursor.execute(com)
     mydb.commit()
  
def updatecountrydesc():
     print("\n")
     c=input('> Enter name of country to be edited :')
     print("\n")
     s=input('> Enter new description :')
     print("\n")
     com="update MAINTABLE set description='{}' where country='{}'".format(s,c)
     mycursor.execute(com)
     mydb.commit()

def displaycustomers():
    com="select * from customerinfo"
    mycursor.execute(com)
    lists=mycursor.fetchall()
    print("\n")
    print(tabulate(lists,headers=["MOBILE","EMAIL","ID","NAME","STATUS"],tablefmt='fancy_grid'))

def customersearch():
    print("\n")
    Id=int(input("Enter booking ID of required customer :"))
    print("\n")
    com="select * from customerinfo where ID='{}'".format(Id)
    mycursor.execute(com)
    lists=mycursor.fetchall()
    print(tabulate(lists,headers=["MOBILE","EMAIL","ID","NAME","STATUS"],tablefmt='fancy_grid'))




    
# START OF PROGRAM #
while True:
     mainmenu()
     if n==0:
         #END PROGRAM
         break
     if n==1:
         #CONSUMER BOOKING
         maintable()
         deco()
         CONSUMERSCREEN1()
         print("\n")
         print("> In order to return to main menu, kindly type 0 in the following field ::")
         print("\n")
         x=int(input("> To plan your itinerary, kindly enter the duration of your stay (in days) :"))
         print("\n")
         if x==0:
             continue
         y=int(input("> Enter number of travellers :"))
         print("\n")
         z=int(input("> Enter number of hotel rooms required :"))
         print("\n")
         deco()
         hotelsandflights()
         deco()
         print("\n")
         print("> In order to return to main menu, kindly type 0 in the following field ::")
         print("\n")
         a=int(input("> Enter 1 to convert into BHD / 2 to convert into USD :"))
         print("\n")
         if a==0:
             continue
         deco()
         conversion=convertor()
         r=conversion[0]
         currency=conversion[1]
         print("\n")
         print("> Total flight cost (for all travellers) is :",totalair*r,currency,"\n")
         print("> Total hotel cost (for all travellers) is :",totalhotel*r,currency,"\n")
         print("> Total cost of trip for all travellers is estimated at :",(totalair*r)+(totalhotel*r),currency)
         print("\n")
         deco()
         print("\n")
         print("> In order to return to main menu, kindly type 0 in the following field ::")
         print("\n")
         mob=int(input("> In order to book your trip, kindly enter your mobile number :"))
         print("\n")
         if mob==0:
             continue
         booking()
         continue
     if n==2:
         #CANCELLATION
         print("\n")
         cancel=input("> In order to cancel your trip, kindly enter your booking ID :")
         cancellation()
         deco()
         print("\n")
         print("> Your booking has been cancelled successfuly","\n")
         print("> The refund shall be made directly to your account ","\n")
         print("> To convey any grievances regarding our services, kindly contact us at team2complaints@gmail.com")
         print("\n")
         print("> You may also contact us at 38726382/36478283")
         print("\n")
     if n==3:
           #EMPLOYEE PROGRAM
           #PASSWORD = '1234’
           deco()
           j=0
           while True:
                 passwd=input("ENTER PASSWORD : ")
                 if passwd!="1234":
                    print('Incorrect')
                    k=int(input("Enter '1' to retry, enter '2' to return to main menu : "))
                    if k==1:
                       deco()
                       continue
                    if k==2:
                       j=1
                       break
                 j=0
                 break
           if j==1:
              continue
           #MENU FOR EMPLOYEES 
           while True:
                 deco()
                 print("\n")
                 exitvariable=0
                 print("> Press '1' to add a new country <","\n")
                 print("> Press '2' to add a new city <","\n")
                 print("> Press '3' to add new tourist attractions <","\n")
                 print("> Press '4' to modify a country description <","\n")
                 print("> Press '5' to modify a city description <","\n")
                 print("> Press '6' to edit conversion rate <","\n")
                 print("> Press '7' to edit a flight multiplier <","\n")
                 print("> Press '8’ to edit a hotel multiplier","\n")
                 print("> Press '9' to edit hotel/airline fares <","\n")
                 print("> Press '10' to view all customer details <","\n")
                 print("> Press '11' to view details of a single customer <","\n")
                 print("> Press ‘12’ if you wish to return to the main menu <","\n")
                 print("\n")
                 deco()
                 choice=int(input("> Kindly enter your choice : "))
                 deco()
                 print("\n")
                  
                 if choice==1:
                    insertcountry()
                 elif choice==2:
                      insertcity(0)
                 elif choice==3:
                      inserttourism(0)
                 elif choice==4:
                      updatecountrydesc()
                 elif choice==5:
                      updatecitydesc()
                 elif choice==6:
                      rateupdate()
                 elif choice==7:
                      editflightmult()
                 elif choice==8:
                      edithotelmult()
                 elif choice==9:
                      updatefares()
                 elif choice==10:
                      displaycustomers()
                 elif choice==11:
                      customersearch()
                 elif choice==12:
                      exitvariable=1
                 else:
                      print("> Invalid choice, please try again ")
                 if exitvariable==1:
                    break
           continue
