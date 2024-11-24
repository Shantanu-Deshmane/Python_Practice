row=int(input("enter a number of rows: "))
for i in range(row+1,1,-1):
    for j in range(0,i-1):
        print("*",end=" ")
    print(" ")

for i in range(0,row):
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")
    