#filer10_20
x=[11,12,31,16,76,3,12,33,19,18,30]
filter10_20=list(filter(lambda a: a>10 and a<20,x))
print(filter10_20)
#filter odd even from list
filter_odd=list(filter(lambda a: a%2==1,x))
print(filter_odd)
filter_even=list(filter(lambda a: a%2==0,x))
print(filter_even)
