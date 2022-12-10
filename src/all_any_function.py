odd=[1,3,5,7,9]
even=[2,4,6,8,10]
print(all([i%2==1 for i in odd]))
print(all([i%2==1 for i in even]))
print(all([i%2==0 for i in odd]))
print(all([i%2==0 for i in even]))
def sum_all(*args):
    if all([(type(arg)==int or type(arg)== float) for arg in args]):
        total=0
        for i in args:
            total=total+i
        return total
    else:
        return "Wrong Input"

print(sum_all(1,3,5,7,9,'a','e','v'))
print(sum_all(1,3,5,7,9))
