# using while loop
row = int(input("Enter rows: "))
i=1
while i<=row:
    j=1
    while j<=i:
        print((i*2-1),end=" ")
        j+=1
    i+=1
    print(" ")
    