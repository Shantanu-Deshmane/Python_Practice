# for i in range(0,6):
#     for j in range(i):
#         print("*", end=" ")
#     print(" ")

# ********************************

for rows in range(4):
    for column in range(4):
        print(rows, end=" ")
    print(" ")

# ********************************
a=1
for rows in range(0,5):
    for columns in range(rows):
        print(a, end=" ")
        a+=1
    print(" ")