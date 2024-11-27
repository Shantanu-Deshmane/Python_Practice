limit=int(input("Enter a number to print series up to : "))
a=0
b=1
print(a,b,end=" ")
for i in range(2,limit):
    c=a+b
    a,b=b,c
    print(c,end=" ")