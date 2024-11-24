a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if a>=b and a>=c :
    print("%d is greater than %d and %d"%(a,b,c))
elif b>=a and b>=c :
    print("%d is greater than %d and %d"%(b,a,c))
else:
    print("%d is greater than %d and %d"%(c,a,b))

