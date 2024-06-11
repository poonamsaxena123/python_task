from functools import reduce
li=[1,2,3,4,5]
sum=reduce(lambda x ,y :x * y ,li)
print(sum)



l2=[4,20,100,70,44]
max_ele=reduce(lambda x, y : x if x > y else y ,l2)
print(max_ele)