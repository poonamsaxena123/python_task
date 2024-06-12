from functools import reduce
# string revese 
reverse_str=lambda s :s[::-1]
print(reverse_str("hello"))

reverse = lambda s: s[::-1]
print(reverse("hello"))  # Output: "olleh"


# filter even numer 
li=[34,5,6,7,8,9,19]
even_no=list(filter(lambda x: x % 2 == 0,li))
print(even_no)

# using map to uppercase
li=["mini","Laves","kunal"]
upper_str=map(lambda s :s.upper(),li)
print(list(upper_str))

# sort the tuple t second element
t1=[(1,3),(4,1),(5,2),(1,10),(5,71)]
sorted_tuple=sorted(t1,key=lambda x : x[1])
print(sorted_tuple)


# sum of sure nume of list
li=[2,3]
sum_of_squre=reduce(lambda x, y :x + y, map(lambda x : x **2, li))
print(sum_of_squre)