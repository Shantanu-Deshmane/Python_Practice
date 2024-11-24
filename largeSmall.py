a=int(input("Enter a first Number: "))
b=int(input("Enter a second Number: "))
c=int(input("Enter a third Number: "))

# code to find largest number
if (a>=b and a>=c): 
    large=a
elif(b>=c and b>=a):
    large=b
else:
    large=c

# code to find smallest number
if (a<=b and a<=c): 
    small=a
elif(b<=c and b<=a):
    small=b
else:
    small=c

print("Largest number is %d"%large)
print("Smallest number is %d"%small)