f=1
a=int(input("The number:"))
if a<0:
    print("There is no Factorial.")
if a==0:
    print("Factorial:",1)
if a>0:
    while 1<=a:
        f=f*a
        a=a-1
    print("The Factorial of that Num:",f)
