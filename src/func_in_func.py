def greater(a,b):
    if a>b:
        return a
    else:
        return b
def greatest(a,b,c):
    x=greater(a,b)
    y=greater(x,c)
    return y
a,b,c=input("Enter Three Number:").split()
a=int(a)
b=int(b)
c=int(c)
x=greatest(a,b,c)
print("The Greatest Number:",x)
