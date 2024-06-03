List = [1,2,3,4,[44,55],[90,88]]
l2=[]
for item in List:
    if isinstance(item,list):
        l2.extend(item)
    else:
        l2.append(item)
l2.sort()
print(l2)