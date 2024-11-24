# x=1
# while x <= 10:
#     print(x)
#     x+=1

# print("number \t square")
# print(".................")
# for i in range(1,11):
#     square=i**2
#     print(i,"\t", square)

# a=1
# for row in range(1,6):                         
#     for column in range(1,row+1):
#         print(a, end=" ")
#         a+=1
#     print()

# ---> OUTPUT 





# for row in range(1,6):                         
#     for column in range(1,row+1):
#         print("*", end=" ")
#     print()

# ---> OUTPUT 
# *
# * *
# * * *
# * * * *
# * * * * *



# for row in range(6,0,-1):
#     for column in range(1,row+1):
#         print("*", end=" ")
#     print()

# --->OUTPUT
# * * * * * *
# * * * * *
# * * * *
# * * *
# * * 
# *

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False 
        return True 
        
for number in range(1,101):
    if is_prime(number):
        print(number)