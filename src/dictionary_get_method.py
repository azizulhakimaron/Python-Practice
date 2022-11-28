d={"name":"aron","age":24}
print(d.get("names"))
if "name" in d:
    print("Present")
else:
    print("Not Present")
if d.get("name"):
    print("Present")
else:
    print("Not Present")
print(d.get("names","Not Found"))
