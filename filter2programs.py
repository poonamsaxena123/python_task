from functools import reduce
#find the  squre of even numer  using filter and map 

li=[2,3,4,5,6,7,8,1,15,10]
li2=list(filter(lambda x : x%2==1 ,li))
l3=map(lambda x : x ** 2,li2)
print(list(l3))



l4=list(map(lambda x : x ** 2,filter(lambda x : x%2==0 ,li)))
print(l4)


# sum of even using filter and reduce


l5= reduce(lambda a, c : a + c, filter(lambda x : x % 2 == 0 ,li))
print(l5)


# find even numer using list comprension
newlist=list(filter(lambda x : x % 2 == 0,li))

