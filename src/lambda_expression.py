add=lambda a,b : a+b
multiply=lambda a,b : a-b
divided=lambda a,b : a/b
power=lambda a,b : a**b
#odd_even
is_even= lambda a: a%2==0
odd_even= lambda a : f'Even:{a}' if a%2==0 else f'Odd:{a}'
print(is_even(3))
print(odd_even(2))
#last_char
last_char=lambda a: a[-1]
print(last_char("Aron"))
#between10_20
btw10_20=lambda a: a>10 and a<20
print(btw10_20(15))
#char length
char_len_check=lambda a: len(a)>5
print(char_len_check("azizul"))
#filer10_20
x=[11,12,31,16,76,3,12,33,19,18,30]
filter10_20=list(filter(lambda a: a>10 and a<20,x))
print(filter10_20)
#filter odd even from list
filter_odd=list(filter(lambda a: a%2==1,x))
print(filter_odd)
filter_even=list(filter(lambda a: a%2==0,x))
print(filter_even)
