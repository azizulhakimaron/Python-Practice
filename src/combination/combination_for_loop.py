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
    for l in range(1,n+1):
        i=l*i
    u=i
    for m in range(1,r+1):
        j=m*j
    v=j
    for o in range(1,x+1):
        k=o*k
    w=k
    y=u/(v*w)
    print("nCr:",y)
