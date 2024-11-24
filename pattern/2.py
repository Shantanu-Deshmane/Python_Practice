#        *
#        **
#        ***
#        ****
#        *****

rows = int(input("Enter a number of rows: "))

# declaring outer loop to handle rows
for i in range(0,rows):
    # declaring inner loop to handle columns
    # Values changes according to outer loop
    for j in range(0,i+1):
        # here we declared for loop to print stars
        print("*",end=" ")
    print(" ")