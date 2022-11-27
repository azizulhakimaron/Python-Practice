 #input a number. If the number is even, print its square otherwise print its cube.
a=int(input("The Number: "))
x=a%2
y=(x!=0)
z=a**2
j=a**3
if y:
    print("The Number is ODD and its Cube:",j)
else:
    print("The Number is EVEN and its square:",z)
