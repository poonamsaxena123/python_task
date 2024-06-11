li=["poonam","rahul","lll","nvm"]
newli=list(filter(lambda element : "a" not in element ,li))
print(newli)


num=[3,4,5,6,1,10]
nli=list(filter(lambda x : x%2==0,num))
print(nli)

people=[
    {"name":"ankit","age":50},
    {"name":"sakhi","age":90},
    {"name":"deep","age":12}
]
li=list(filter(lambda word : word['age']>30 ,people))
print(li)

objects = [0, 1, [], 4, 5, "", None, 8]

print(list(filter(None, objects)))
[1, 4, 5, 8]