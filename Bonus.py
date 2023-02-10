#bonus amount
salary=int(input("enter the salary"))
years=int(input("enter the year of service"))
if(years>10):
    bonus=salary*0.1
    print("then bonus will be 10%")
if(years>=6 and years<=10):
     bonus=salary*0.08
     print("then bonus will be 8%")
if(years<6):
     bonus=salary*0.05
     print("then bonus will be 5%")