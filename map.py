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