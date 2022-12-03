#Position Tracker
x=["a","b","c","d"]
pos=0
for i in x:
    print(f"{pos}={i}")
    pos=pos+1
#using enumerate function
for pos,i in enumerate(x):
    print(f"{pos}={i}")
