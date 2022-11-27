#1+(x^2/2!)+(x^4/4!)+......
import math as m
x=int(input("Enter the value of x:"))
n=int(input("How many step do you want to run:"))
sum=0
for i in range(1,n+1):
    y=2*i-2
    i=(m.pow(x,y))/(m.factorial(y))
    sum=sum+i
print("The Sum:%.4f"%sum)
