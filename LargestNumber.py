#largest of the three
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if(a>b and a>c):
    print("then a is greater than b and c")
elif(b>a and b>c):
    print("then b is greater than b and c")
else:
    print("then c is the largest")