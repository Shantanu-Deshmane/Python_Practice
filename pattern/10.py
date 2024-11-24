rows=int(input("Enter a number of rows: "))
for i in range(rows,0,-1):
    a=i
    for i in range(0,i):
        print(a, end=" ")
    print(" ")