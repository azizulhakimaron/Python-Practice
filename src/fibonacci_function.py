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
x=fibonacci(10)
print(x)
    

