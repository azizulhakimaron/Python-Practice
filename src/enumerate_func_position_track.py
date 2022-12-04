def pos_track(l,target):
    for pos,i in enumerate(l):
        if i==target:
            return pos
x=["a","b","c","d"]
print(pos_track(x,"c"))
