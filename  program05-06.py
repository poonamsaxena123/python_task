s1={3,4,5,6,7}
print(s1)
s={10,"aa"}
s.add(109)

s.pop()
s1.remove(4)

print(s)
print(s1)

s1.discard(7)
print(s1)

# Q1 sort dictionaty y key value d

d={"poonam":10,"neha":5,"anu":20}

my_dict =list(d.keys())
my_dict.sort()          # using sort metrhod of list
d={i : d[i] for i in my_dict}
print(d)
for i in sorted(d.keys()):    # using sorted method of 
     print((i,d[i]) ,end="")