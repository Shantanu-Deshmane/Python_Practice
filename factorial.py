num = int(input("Enter a number to find a factorial : "))
factorial = 1
for i in range(1,num+1):
    factorial = factorial * i
print(f"Factorial of {num} is : {factorial}")