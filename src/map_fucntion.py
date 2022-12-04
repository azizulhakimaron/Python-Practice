x=[1,2,3,4,5,6,7,8,9,10]
def square(a):
    return a**2
def cube(a):
    return a**3
def odd(a):
    return 2*a-1
def even(a):
    return 2*a
def odd_1(a):
    if a%2==1:
        return a
sqr=list(map(square,x))
print(sqr)
cube1=list(map(cube,x))
print(cube1)
odd1=list(map(odd,x))
print(odd1)
even1=list(map(even,x))
print(even1)
odd12=list(map(odd_1,x))
print(odd12)
