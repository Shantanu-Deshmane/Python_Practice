row=int(input("Enter a number of rows: "))
for i in range(0,row):
    a=0
    for j in range(0,i+1):
        a+=1
        print(a,end=" ")
    print(" ")