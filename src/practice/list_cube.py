a=[1,2,3,4,5,6,7,8,9]
x=[]
for i in a:
    x.append(i**3)
print(x)

#cube_list
def cube_list(l):
    x=[]
    for i in l:
        x.append(i**3)
    return x
z=cube_list(a)
print(z)