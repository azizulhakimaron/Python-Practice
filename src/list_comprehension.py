#list comprehension
square=[i**2 for i in range(1,11)]
negetive=[-i for i in range(1,11)]
root=[i**.5 for i in range(1,11)]
print(f"Square:{square}\nRoot:{root}\nNegetive:{negetive}")
#print first char
name=["aron","kasab","somoy","mukit","omio"]
first_char=[i[0] for i in name]
print(first_char)
#reverse string
reverse=[i[::-1] for i in name]
print(reverse)
#if else statement
num=list(range(1,11))
odd=[i for i in num if i%2==1]
even=[i for i in num if i%2==0]
print(odd)
print(even)
