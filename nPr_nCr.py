# nPr = n! / (n-r)!
# nCr = n! / (r!(n-r)!)

# Function to find factorial
def factorial(n):
    fact=1
    for i in range (n,1,-1):
        fact*=i
    return fact
# function to find nPr 
def nPr(n,r):
    result = factorial(n) // factorial(n-r)
    print(f"Value of nPr is : {result}")

# function to find nCr 
def nCr(n,r):
    result = factorial(n) // (factorial(r)*factorial(n-r))
    print(f"Value of nCr is {result}")

n=int(input("Enter a value of n : "))
r=int(input("Enter a value of r : "))

nPr(n,r)
nCr(n,r)