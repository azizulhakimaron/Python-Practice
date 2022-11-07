sum=0
a,b=input("Range").split()
a=int(a)
b=int(b)
if a%2==0:
    a=a+1
    while a<=b:
        sum=a+sum
        a=a+2
    print("Sum:",sum)
if a%2==1:
    
    while a<=b:
        sum=sum+a
        a=a+2
    print("Sum:",sum)
