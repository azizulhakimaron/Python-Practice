import aron_function as af
import numpy as np
def cart_polar(a,b):
    x=np.power(a,2)+np.power(b,2)
    r=np.power(x,.5)
    y=(b/a)
    y=af.mod1(y)
    if a>0 and b>0:
        q1=af.arctan_d(y)
        return r,q1
    if a<0 and b>0:
        q2=180-af.arctan_d(y)
        return r,q2
    if a<0 and b<0:
        q3=180+af.arctan_d(y)
        return r,q3
    if a>0 and b<0:
        q4=-af.arctan_d(y)
        return r,q4
    if a==0 and b>0:
        q5=90
        return r,q5
    if a>0 and b==0:
        q6=0
        return r,q6
    if a==0 and b<0:
        q7=180
        return r,q7
    if b==0 and a<0:
        q8=180
        return r,q8
x,y=input("The Cartesian point:").split()
x=float(x)
y=float(y)
z=cart_polar(x,y)
print("The Polar point:",z)
