#  q1 L pattern 
# def l_pattern(n):
#     for i in range(n):
#         if i < n-1:
#             print('* ')  
#         else:
#             print('* '*n ) 


# num=int(input("enter the rows  "))
# l_pattern(num)


# q2 half paramid

# num=5

# for i in range(num+1):
#     print("* "*i)
       


# q3 full pyramid

rows = int(input("Enter the number of rows: "))  
for i in range(0, rows):  

        for j in range(0, rows):  
            print(end=" ")
        rows -= 1 
        for j in range(0, i+1):  
            print("*",end=" ")              
  
        print()

