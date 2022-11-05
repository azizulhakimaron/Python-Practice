a,b,c=input("Three Sides Of Triangle:").split()
a=int(a)
b=int(b)
c=int(c)
if a+b>c and c+a>b and c+b>a :
    print("The Triangle Exist")
else:
    print("The Triangle Doesnt Exist")
