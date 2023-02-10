#Grading system
sub1=int(input("enter the marks"))
sub2=int(input("enter the marks"))
sub3=int(input("enter the marks"))
score=((sub1+sub2+sub3)/3)
if(score>=70 and score<=100):
    print("Grade A", A)
if(score>=60 and score<=69):
    print("Grade B", B)
if(score>=50 and score<=59):
    print("Grade C", C )
if(score>=40 and score<=49):
    print("Grade D", D )
if(score>=0 and score<=39):
    print("FAIL")
else:
    print("INVALID MARKS")