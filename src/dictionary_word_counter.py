word=input("Enter The Word:")
count={}
for i in word:
    count[i]=word.count(i)
print(count)
#word_count
def word_count(a):
    count={}
    for i in a:
        count[i]=a.count(i)
    return count
x=word_count('azizul')
print(x)
