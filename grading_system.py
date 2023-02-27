#grading system using a function
from re import A


def get_grading_system (sub1=70,sub2=69,sub3=40):
    sub1=int(input("enter the marks of the subject one;"))
    sub2=int(input("enter the marks of the subject two;"))
    sub3=int(input("enter the marks of the third subject;"))
    score=((sub1+sub2+sub3)/3)
    if score>=70 and score<=100:
        print("grade A",A)
    elif score>=60 and score<=69:
        print("grade B",B)
    elif score>=50 and score<=59:
         print("grade C",C)
    elif score>=40 and score<=49:
        print("grade D",D)
    elif score>=0 and score<=39:
        print("FAIL")
    else:
        print("REPEATE!")
    get_grading_system()
