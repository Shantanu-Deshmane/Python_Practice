a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))

while a !=b :
    if a>b:
        a-=b
    else:
        b-=a

print("gcd of entered numbers is: ",b)
