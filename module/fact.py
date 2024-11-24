# Calculating the nCr and nPr using module
import factorial1

def nPr(n,r):
    result= factorial1.factorial(n) // factorial1.factorial(n-r)
    print("nPr of entered data is: ",result)

def nCr(n,r):
    result=factorial1.factorial(n) // (factorial1.factorial(r)*factorial1.factorial(n-r))
    print("nCr of entered data is: ",result)

n=int(input("Enter a value for n: "))
r=int(input("Enter a value for r: "))

nPr(n,r)
nCr(n,r)