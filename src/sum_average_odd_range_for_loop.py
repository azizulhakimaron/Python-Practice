sum=0
a,b=input("Range:").split()
a=int(a)
b=int(b)
p=((b-a)/2)+1
o=(b-a+1)/2
n=(b-a+1)/2
m=(b-a)/2
if a%2==0 and b%2==0:
    for i in range(a+1,b,2):
        sum=sum+i
    print("Sum",sum)
    z=sum/m
    print("Averege:",z)
if a%2==0 and b%2==1:
    for i in range(a+1,b+1,2):
        sum=sum+i
    print("Sum",sum)
    z=sum/n
    print("Average:",z)
if a%2==1 and b%2==0:
    for i in range(a,b+1,2):
        sum=sum+i
    print("Sum:",sum)
    z=sum/o
    print("Average:",z)
if a%2==1 and b%2==1:
    for i in range(a,b+1,2):
        sum=sum+i
    print("Sum:",sum)
    z=sum/p
    print("Average:",z)

        