import math as m
x=int(input("Enter the value of x:"))
n=int(input("How many step do you want to run:"))
sum=0
for i in range(0,n):
    i=(m.pow(x,i))/(m.factorial(i))
    sum=sum+i
print("The Series Value:%.4f"%sum)