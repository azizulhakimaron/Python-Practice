a=list(range(1,101))
x=[]
for i in a:
    x.append(i**2)
print(x)
#squrare_list
def square_list(l):
    x=[]
    for i in l:
        x.append(i**2)
    return x
z=square_list(a)
print(z)