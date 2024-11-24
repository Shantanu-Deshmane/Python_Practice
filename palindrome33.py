# a=input("Enter a number to check palindrome: ")
# for i in a:
#     b=(a[ ::-1])
# if a == b:
#     print("Entered data is PALINDROME")
# else:
#     print("Entered data is NOT PALINDROME")

# print(type(a))
# print(type(b))
    
a=input("Enter a number to check palindrome: ")
b=a[ :: -1]
if a == b:
    print("Entered data is PALINDROME")
else:
    print("Entered data is NOT PALINDROME")
