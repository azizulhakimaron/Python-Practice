
def mod1(a):
    if a>0:
        return a
    else:
        b=a*(-1)
        return b
def greater(a,b):
    if a>b:
        return a
    else:
        return b
def mod2(a):
    x=a*(-1)
    y=greater(a,x)
    return y
a=float(input("Enter The Number:"))
x=mod1(a)
y=mod2(a)
print(f"The Modulus:{x}\nThe Modulus:{y}")
