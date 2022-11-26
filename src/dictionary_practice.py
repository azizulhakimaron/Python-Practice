a=int(input("The Range:"))
b={}
for i in range(1,a+1):
    x=i**3
    b[i]=x
print(b)
#dict_cude_finder
def dict_cube_finder(a):
    b={}
    for i in range(1,a+1):
        b[i]=i**3
    return(b)
y=dict_cube_finder(8)
print(y)