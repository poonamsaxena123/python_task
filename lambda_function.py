val=lambda x: x + 1
print(val(2))

full_name=lambda first ,last : f"full name :{first.title()} {last.title()}"
print(full_name("poonam", "saxena"))


print((lambda x, y : x + y)(1, 2))

higher_order= lambda x, func : x + func(x)
print(higher_order(2, lambda y : y * y))

print((lambda x: "odd" if x % 2 else "even")(2))

#positional argument

print((lambda x, y, z : x + y + z)(1, 2, 3))

# named argument 

print((lambda x, y, z = 3: x + y + z)(1,2))

#variale list argumnet 

print((lambda *args: sum(args))(2,3,4,))

print((lambda **kwargs: sum(kwargs.values()))(one=1,two=2,three=3))

print((lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3))

li=[1,2,3,4]
squre= (lambda x : x **2 ,li)
print(squre)

lst_check = ['word', 'test', 'window', 'example']

# next func

add  = lambda a : a + 10
print(add(5))
