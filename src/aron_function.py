#arcsin_d()
import numpy as np
def arcsin_d(a):
    x=np.arcsin(a)
    y=np.degrees(x)
    return y
#arccos_d()
def arccos_d(a):
    x=np.arccos(a)
    y=np.degrees(x)
    return y
#arctan_d()
def arctan_d(a):
    x=np.arctan(a)
    y=np.degrees(x)
    return y
#mod1
def mod1(a):
    if a>0:
        return a
    else:
        b=a*(-1)
        return b
#greater
def greater(a,b):
    if a>b:
        return a
    else:
        return b
#mod2
def mod2(a):
    x=a*(-1)
    y=greater(a,x)
    return y
#area_tri1
import numpy as np
def area_tri1(a,b,c):
    s=(a+b+c)/2
    A=(s*(s-a)*(s-b)*(s-c))**.5
    return A
#area_tri2
def area_tri2(a,b,x):
    A1=(.5)*a*b*(np.sin(x))
    return A1
#odd_even
def odd_even(number):
    if number%2==0:
        return "Even"
    else:
        return "Odd"
#cart_polar
def cart_polar(a,b):
    x=np.power(a,2)+np.power(b,2)
    r=np.power(x,.5)
    y=(b/a)
    y=mod1(y)
    if a>0 and b>0:
        q1=arctan_d(y)
        return r,q1
    if a<0 and b>0:
        q2=180-arctan_d(y)
        return r,q2
    if a<0 and b<0:
        q3=180+arctan_d(y)
        return r,q3
    if a>0 and b<0:
        q4=-arctan_d(y)
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
#fibonacci()     
def fibonacci(z):
    a=0
    b=1
    if z==1:
        print(a)
    if z==2:
        print(a,b)
    if z>2:
        print(a,b,end=" ")
        for i in range(z-2):
            c=a+b
            a=b
            b=c
            print(b,end=" ")

