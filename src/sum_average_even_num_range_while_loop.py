sum=0
a,b=input("Range:").split()
a=int(a)
b=int(b)
m=((b-a)/2)+1
n=((b-a-1)/2)+1
o=(b-a+1)/2
p=(b-a)/2
if a%2==0:
    while a<=b:
        sum=sum+a
        a=a+2
    print("Sum:",sum)
    if b%2==0:
        z=sum/m
        print("Average:",z)
    if b%2==1:
        z=sum/n
        print("Average:",z)
if a%2==1:
    a=a+1
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
