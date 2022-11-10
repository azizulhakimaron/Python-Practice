import math as m
x=int(input("Enter the value of x:"))
n=int(input("How many step do you want to run:"))
sum=0
for i in range(1,n+1):
    i=((m.pow(x,2*i-1))/(m.factorial(2*i-1)))*(m.pow(-1,i-1))
    sum=sum+i
print("Sinx:%.4f"%sum)