a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))
c=int(input("Enter a third number: "))
def largest_num(a,b,c):
    if a>b and a>c:
        print(f"{a} is greater than {b} and {c}")
    elif b>c and b>a:
        print(f"{b} is greater than {a} and {c}")
    else:
        print(f"{c} is greater than {a} and {b}")

largest_num(a,b,c)