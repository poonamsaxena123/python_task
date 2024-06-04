#tuple

t=(2,3,4,5,"poonam",2)
t2=(6,77,1000,10)
l=[6,3,6,78]
print(t[2])
print(t.index(2))

print(t.count(2))
t3=t+t2
print(t3)
tt=tuple(("av","v","c","d"))
print(len(tt))
print(tt[::-1])
if "v" in tt:
    print("yes")
newt=list(tt)
newt[2]="mongo"
print(tuple(newt))

newt.append("cherry")
print(tuple(newt))

newt.remove("av")
print(tuple(newt))
# unpacking of tuples
a,c,*d=newt
print(a,c,d)


# set opreations
s={2,3,4,5,"poonam","saxena",200,False,0}
s={12,78,"va"}
print("$$$$$",s)
print(len(s))

for item in s:
    print(item)
d={10:"poonam"}
s.add(500)

s.update(newt)
s.update(d)
print(s)

s.discard(2)
print(s)
# s.remove(4)
print(s)
s1={1,2,3,4}
s2={4,3,5,6,7}
s3=s1 | s2
print(s3)

print(next(iter(s3)))
s4=s1.intersection(newt)
print(s4)
if  3 in  s2:
    element=3
    print("&&&&",element)

my_set = {1, 2, 3, 4, 5}
element = next((x for x in my_set if x > 2))
print("@@@",element)  # This will print the first element greater than 2


# dictionary
d={"name":"akash","phno":989479734,"email":"hkdshh"}
print(len(d))
print(d["name"])
print(d.get("email"))

print(d.keys())

print(d.values())

d["age"]=23
print(d.items())

p=d.pop("age")
print(p)
print(d)

pit=d.popitem()
print(pit)

for key,value in d.items():
    print(key,value)

d1=dict(d)
d1["age"]=67
print("!!!!",d1)
print(d)