rows=int(input("Enter number of rows: "))
a=0
for i in range(0,rows):
    a+=1
    for j in range(0, i+1):
        print(a, end=" ")
    print(" ")