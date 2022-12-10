def average_finder(*args):
    avg=[]
    for i in args:
        avg.append(sum(i)/len(i))
    return avg

average_finder1=lambda *args:[sum(i)/len(i) for i in zip(*args)]
print(average_finder([1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]))
print(average_finder1([1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]))