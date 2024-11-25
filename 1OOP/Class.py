class GCD:
    a=int(input("Enter a first number: "))
    b=int(input("Enter a Decond number: "))
    while a != b :
        if a>b:
            a-=b
        else:
            b-=a

result=GCD()
print("GCD of entered numbers is: ", result.a)
