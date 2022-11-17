sum=0
a,b=input("Range").split()
a=int(a)
b=int(b)
p=((b-a)/2)+1
o=(b-a+1)/2
n=(b-a+1)/2
m=(b-a)/2
if a%2==0:
    a=a+1
    while a<=b:
        sum=a+sum
        a=a+2
    print("Sum:",sum)
    if b%2==0:
        z=sum/m
        print("Averege:",z)
    if b%2==1:
        z=sum/n
        print("Average:",z)
if a%2==1:
    while a<=b:
        sum=sum+a
        a=a+2
    print("Sum:",sum)
    if b%2==0:
        z=sum/o
        print("Average:",z)
    if b%2==1:
        z=sum/p
        print("Average:",z)
