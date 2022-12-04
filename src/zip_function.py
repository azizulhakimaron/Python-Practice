user=['user1','user2','user3','user4']
name=['aron','kasab','mukit','somoy']
#x=[1,2,3,4]
x=zip(user,name)
y=list(x)
print(y)
print(dict(y))
#unpack with * 
l=[(1,2),(2,4),(3,6),(4,8)]
l1,l2=list(zip(*l))
print(list(l1))
print(list(l2))
a=[1,2,3,4]
b=[2,4,6,8]
x1=[]
for i in zip(a,b):
    x1.append(max(i))
print(x1)