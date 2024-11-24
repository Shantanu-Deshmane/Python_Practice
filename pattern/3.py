row = int(input("Enter number of rows: "))
# declared outer loop for rows
for i in range(row+1,0,-1):

    # declared inner loop for column
    for j in range(0,i-1):
        print("*", end=" ")
    print("")