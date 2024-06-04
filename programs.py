# 1. program to interchange first item to last item
li=[6,7,1,2,9]
size=len(li)

temp=li[0]
li[0]=li[size-1]
li[size-1]=temp
print(li)

# 2.remove empty list from list

l2=[6,7,54,3,[],[6,90]]
l=[i  for i in l2 if i !=[]]

print(l)

# 3. largest and smollest in list

def largest_smollest(li):

    minn=min(li)
    large=max(li)
    return minn,large
print(largest_smollest([1,2,3,4,5,8,19,199]))

# 4. palindrom

def is_palindrom(li):
    left,right=0,len(li)-1
    while left<right:
        if li[right]!=li[left]:
            return "this is not palindrom"
        left+=1
        right-=1
    return " this is palindrom"



print(is_palindrom([1, 2, 3, 2, 1,7]))


# 5.remove duplicates from list

def remove_duplicate(list1):
    # return set(list1)
    l2=[]
    for i in range(0,len(list1)):
        if list1[i] not in  l2:
            l2.append(list1[i])
    return l2

print(remove_duplicate([11,3,3,11,4,5,5]))

# 6. reverse a numer

def reverse_num(num):
    newnum=0
    while num!=0:
        rev =num%10
        newnum=newnum*10+rev
        num=num//10
    print(newnum)


reverse_num(3456)