def squer(n):
    return n ** 2

li=[3,4,5,1,6,8]

numer_squre=map(squer,li)
print(list(numer_squre))

squer_list=map(lambda x : x**2 ,li)
print(list(squer_list))


li2=[7,5,6,3,2,3]
sum=map(lambda x,y : x + y ,li,li2)
print(list(sum))


# covert string to integer
st=['1','2','3','4'] 
convert_iteger=list(map(lambda s: int(s), st))
print(convert_iteger)


# appply a function of each element
l1=[6,7,8,5,4]
result= map(lambda x : x +3,l1)
print(list(result))

# calculat the length of each string 
sst=["kivi","nimooo","naa","apple"]
lengthfind=map(lambda s : len(s) ,sst )
print(list(lengthfind))