import numpy as np
def area_tri1(a,b,c):
    s=(a+b+c)/2
    A=(s*(s-a)*(s-b)*(s-c))**.5
    return A
def area_tri2(a,b,x):
    A1=(.5)*a*b*(np.sin(x))
    return A1
p=input("1.Three Arms are given.\n2.Two arms and intersection angle is given.\nEnter the 1 or 2:")
p=int(p)
if p==1:
    x,y,z=input("Three Arms").split()
    x=int(x)
    y=int(y)
    z=int(z)
    A=area_tri1(x,y,z)
    print("Area of Triangle:",A)
if p==2:
    x1,y1,z1=input("First Enter 2 Arms and Angle(Degree):").split()
    x1=int(x1)
    y1=int(y1)
    z1=int(z1)
    z1=np.radians(z1)
    A1=area_tri2(x1,y1,z1)
    print("Area of Triangle:",A1)
