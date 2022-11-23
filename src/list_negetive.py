a=[1,2,3,4,5,6,7,8,10]
x=[]
for i in a:
    x.append(-i)
print(x)
def neg_list(l):
    x=[]
    for i in l:
        x.append(-i)
    return x
z=neg_list(a)
print(z)