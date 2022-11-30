#if else statement
num=list(range(1,11))
odd=[i for i in num if i%2==1]
even=[i for i in num if i%2==0]
print(odd)
print(even)
list1=[i**2 if (i%2==0) else -i for i in num]
print(list1)