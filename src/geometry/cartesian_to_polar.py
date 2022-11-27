import numpy as np
def arcsin_d(a):
    x=np.arcsin(a)
    y=np.degrees(x)
    return y
def arccos_d(a):
    x=np.arccos(a)
    y=np.degrees(x)
    return y
def arctan_d(a):
    x=np.arctan(a)
    y=np.degrees(x)
    return y
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
x,y=input("The Cartesian value:").split()
x=float(x)
y=float(y)
a=np.power(x,2)+np.power(y,2)
r=np.power(a,.5)

if x>0 and y>0:
    b=(y/x)
    b=mod1(b)
    q=arctan_d(b)
    print(f"The Polar point:({r},{q})")
if x<0 and y>0:
    b=(y/x)
    b=mod1(b)
    q=180-arctan_d(b)
    print(f"The Polar point:({r},{q})")
if x<0 and y<0:
    b=(y/x)
    b=mod1(b)
    q=180+arctan_d(b)
    print(f"The Polar point:({r},{q})")
if x>0 and y<0:
    b=(y/x)
    b=mod1(b)
    q=-arctan_d(b)
    q1=360-arctan_d(b)
    print(f"The Polar point:({r},{q})\nOr\nThe Polar point:({r},{q1})")
if x==0 and y>0:
    print(f"The Polar point:({r},90)")
if x>0 and y==0:
    print(f"The Polar point:({r},0)")
if x<0 and y==0:
    print(f"The Polar point:({r},180)")
if x==0 and y<0:
    print(f"The Polar point:({r},270)")
