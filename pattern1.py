num=int(input("enter a rows value "))

for i in range(0,num):
    for j in range(num): 
        print(end=" ")
    num-=1

    for j in range(0,i+1):
        print("*")
        i+=1