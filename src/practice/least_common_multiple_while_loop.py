a,b=input("Two Number for LCM").split()
a=int(a)
b=int(b)
x=max(a,b)
while True:
    if (x%a==0 and x%b== 0):
        break
    x=x+1
print("LCM:",x)
