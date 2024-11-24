rows = int(input("Enter number of rows : "))
a=0
for i in range(rows,0,-1):
    a+=1
    for j in range(0,i):
        print(a,end=" ")
    print(" ")