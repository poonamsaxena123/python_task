from functools import reduce

li=[1,2,3,4,5]
product=reduce(lambda x ,y :x * y ,li)
print(product)



l2=[4,20,100,70,44]
max_ele=reduce(lambda x, y : x if x > y else y ,l2)
print(max_ele)


# sum of evev numer using 

sum_even=reduce(lambda x, y : x + y if not y % 2 else x ,li,0)
print("----",sum_even)

# calculate factorial 

factorial =lambda n :reduce(lambda x ,y : x * y, range(1,n+1))
print(factorial(5))

# concadination of string 

str=["is","mylive","location"]
word=reduce(lambda x, y :x+" "+y ,str) 
print(word)

# flaten a list of list 

l2 =[[1],[1,3,4,6],[5,7],[9,5]]
flat_list=sorted(reduce(lambda x, y : x+y ,l2))
print(flat_list)


#find the longest string 

word=["apple","nanana","chery","oran","watermelon","yasdfghkw"]
st=reduce(lambda x, y: x if len(x) > len(y) else y ,word)
print(st) 


numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y**2, numbers)
print(result)  # Output: 30
