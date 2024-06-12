from functools import reduce
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers,reverse=True)
print(sorted_numbers)  # Output: [1, 2, 5, 5, 6, 9]



li=["apple","cherry","anana","mongo","pop","cacac"]
l2=sorted(li,key=len)
print(l2)

# sort a dic y key

d= [{"name":"kar","age":43},{"name":"depi","age":56},{"name":"pooja","age":10}]
sorted_di=sorted(d ,key=lambda x : x['age'])
print(sorted_di)

# sort a list of list y sum
l2=[[3,4],[9,0],[1,2],[2,10],[3,3]]
print(sorted(l2,key=sum))