s=0
a,b=input("Range").split()
a=int(a)
b=int(b)
y=b-a
while a<=b:
    s=s+a
    a=a+1
print("The Sum",s)
z=s/(y+1)
print("The Average",z)
