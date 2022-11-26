a=[1,2,3,4,5,6,7,8,9,12]
x=[]
y=[]
for i in a:
    if i%2==0:
        x.append(i)
 
for i in a:
    if i%2==1:
        y.append(i)
z=[x,y]
print(z)
#list_odd_even
def list_odd_even(l):
    x=[]
    y=[]
    for i in l:
        if i%2==0:
            x.append(i)
        if i%2==1:
            y.append(i)
    z=[x,y]
    return z
print(list_odd_even(a))

