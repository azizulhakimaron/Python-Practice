b=["abc","efg","xyz"]
u=[]
for i in b:
    v=i[::-1]
    u.append(v)
print(u)
#reverse_string_reverse
def list_string_reverse(l):
    x=[]
    for i in l:
        y=i[::-1]
        x.append(y)
    return x

x=list_string_reverse(b)
print(x)
