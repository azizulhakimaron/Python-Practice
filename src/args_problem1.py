def power(power,*args):
    if args:
        return [i**power for i in args]
    else:
        return "No Args"
n=[1,2,3,4,5,6]
print(power(3,*n))
