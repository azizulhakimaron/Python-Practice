#1+3+5+....
#using while loop
s=0
i=1
a=int(input("The Value Of 'n'"))
x=(2*a)-1
while i<=x:
    s=s+i
    i=i+2
print("The Sum",s)