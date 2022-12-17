c={
    "name":"Aron",
    "age":26,
    "fruits":['apple','orange'],
    "sports":['football','cricket'],
}
#key
if "name" in c:
    print("present")
for i in c:
    print(i)
a1=c.keys()
print(a1)
#value
if 24 in c.values():
    print("present")
for i in c.values():
    print(i)
a=c.values()
print(a)
for i in c:
    print(c[i])



