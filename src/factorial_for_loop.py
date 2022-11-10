a=int(input("Factorial Of Number:"))
f=1
if a<0:
    print("There is no Factorial.")
if a==0:
    print("Factorial:",1)
if a>0:
    for i in range(1,a+1):
        f=f*i
    print("Factorial:",f)
