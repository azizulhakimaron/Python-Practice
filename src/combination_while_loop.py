i=1
j=1
k=1
n,r=input("The n,r for Combination:").split()
n=int(n)
r=int(r)
x=(n-r)
if n<r:
    print("The nCr:",0)
if n>=r:
    while 1<=n:
        i=i*n
        n=n-1
    m=i
    while 1<=r:
        j=j*r
        r=r-1
    o=j
    while 1<=x:
        k=x*k
        x=x-1
    p=k
    y=m/(o*(p))
    print("nCr:",y)
