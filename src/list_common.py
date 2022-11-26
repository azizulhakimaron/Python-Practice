a=[1,2,3,4]
b=[1,2,3,8]
x=[]
for i in a:
    if i in b:
        x.append(i)
print(x)
#list_common
def list_common(a,b):
    x=[]
    for i in a:
        if i in b:
            x.append(i)
    return x
print(list_common(a,b))
