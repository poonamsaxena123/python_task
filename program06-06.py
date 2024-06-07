 #q1 sum of items in dic
def sum_of_dict(dict1,dict2):
     print(dict1,dict2)
     sum=0
     for i ,j in dict2.values(),dict1.values():
          sum=i+j+sum
     print(sum)


dict1={"a":20,"c":2}
dict2={"x":100,"y":40}
sum_of_dict(dict1,dict2)


#q2 print even odd numers 

li=[1,2,3,4,5,6,7,8,9,10]
l3=[]
l3=["even " if i%2==0 else "odd" for i in li] 
print(l3)



# q3 print the squre root 
print("squre root",[ i*2 for i in range(1,10)]) 


# q4 find the length of words
li=["apple","a","cheryy"]
print([len(i) for i in li ])



#5 gives all posiles cominations

print([ (i,j) for i in range(1,7) for j in range(1,7)])


# 6find the common element t two list

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = [x for x in list1 if x in list2]
print(common)


# 7 list of tuple

print([(i ,i**2) for i in range(1,11) ])

# 8 list of stinr length max 3

li=["poonam","a","ranu","kaj","su"]
print([i for i in li if len(i)>3]) 


# 9 list of list
li=[[7,6,8],[10,2,9],[4,3,2,1,4]]
l2=[outer for s_list in li for outer in s_list]
print(l2)


#
# list of prime numer 1 to 100
# List of prime numbers from 1 to 100
primes = [num for num in range(2, 101) if all(num % j != 0 for j in range(2, num))]

print(primes)



