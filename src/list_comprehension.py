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
#nested list comprehension
nested=[[i for i in range(1,4)] for j in range(3)]
print(nested)