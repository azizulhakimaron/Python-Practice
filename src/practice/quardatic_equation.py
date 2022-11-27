#compare to this equation ax^2+bx+c=0
a,b,c=input("The Value Of a,b,c").split()
a=float(a)
b=float(b)
c=float(c)
y=(b**2)-(4*a*c)
x1=(-b+(y**.5))/(2*a)
x2=(-b-(y**.5))/(2*a)
x3=(-b)/(2*a)
if y>0:
    print("The Roots are",x1,x2)
if y==0:
    print("The Roots are",x3)
if y<0:
    print("The Imaginary Number")
