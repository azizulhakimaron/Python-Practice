sum=0
a,b=input("Range:").split()
a=int(a)
b=int(b)
for i in range(a,b+1):
    sum=sum+i
print("Sum:",sum)
