#Input a number and find that its even or odd.
a=int(input("The Number"))
x=a%2
y=(x!=0)
if y:
    print("The Number is ODD")
else:
    print("The Number is EVEN")
