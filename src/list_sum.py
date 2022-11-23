a=[1,2,3,4,5,6,7,8,9]
y=0
for i in a:
    y=y+i
print(y)
#sum_list
def sum_list(l):
    sum=0
    for i in l:
        sum=sum+i
    return (sum)
z=sum_list(a)
print(z)