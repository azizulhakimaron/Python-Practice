#print square
square={f"Square of {n} is":n**2 for n in range(1,11)}
print(square)
#string count
s="azizul"
s_count={i:s.count(i) for i in s}
print(s_count)
#if else
dict={i:('even' if i%2==0 else 'odd') for i in range(1,11)}
print(dict)