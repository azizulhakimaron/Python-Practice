a=int(input("The First Number:"))
b=int(input("The Second Number:"))
c=int(input("The Third Number:"))
if a>=b and a>=c:
    print("Maximum Integer:",a)
if b>=c and b>=a:
    print("Maximum Integer:",b)
if c>=b and c>=a:
    print("Maximum Integer:",c)
