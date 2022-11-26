c={
    "name":"Aron",
    "age":26,
    "fruits":['apple','orange'],
    "sports":['football','cricket'],
}
c1=c.items()
print(c1)
print(type(c1))
for key,value in c.items():
    print(f"Key is {key} and Value is {value}")
