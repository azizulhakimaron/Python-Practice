a=int(input("The Year:"))
x=((a%4==0)and((a%400==0)or(a%100!=0)))
if x:
    print(a,"is Leap Year")
else:
    print(a,"is not Leap Year")
