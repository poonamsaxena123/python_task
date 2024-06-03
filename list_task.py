import copy
# list methods 
li=[6,9,1,0,2]
l2=[100,200,40]
li.append(10) # add the element at last
print(li)

li.insert(1,99) # insert at the index 1 element 99
print(li)  
li.extend(l2) # append list in list or any data
print(li)
try:
    li.remove(11)  # remove first occurence if not exist then it give error value error
    print(li)
except ValueError as e:
    print(f" that element  {e}")

li.pop()   # remove element given index if index is not given then it remove from last
print(li)

del li[2]   # remove element y index 
print(li)

# li.clear()  # clear whole list ut list exist
for item in range(len(li)) :
   print(li[item])
l=["apple","mango","kivi"]
newlist=[x  for x in l if "a" in x] # list connfrension
print(newlist)
li.sort(reverse=True)
print(li)
li3=list(reversed(li)) # itratore method 
print(li3)

liii=li.copy()        # copy method 
print("------",liii)

li.append(50)
print(li)
print("------",liii)

new_list=[45,[1,23],9]
l_new=copy.deepcopy(new_list)
print(l_new)


t=(5,6,7,10,8,2)
print(t[5])
s={3,4,1,8}
print(s)