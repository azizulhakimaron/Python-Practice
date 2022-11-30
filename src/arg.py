#*arg(all_total(1,2,3,4))
def all_total(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
print(all_total(1,2,3,4,5,6,7,8,9,10))
#*arg(all_multiply(1,2,3,4))
def all_multiply(*args):
    m=1
    for i in args:
        m=m*i
    return m
print(all_multiply(1,2,3,4,5))
#for list and tuple.
num1=[1,2,3,4,5,6,7]
num2=(2,8,9,7,5,7)
x1=all_multiply(*num1)#(*) use for list and tuple
x2=all_multiply(*num2)
print(x1)
print(x2)
