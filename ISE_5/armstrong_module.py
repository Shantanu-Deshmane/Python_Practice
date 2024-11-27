from armstrong_fnc import sum_cube
num=int(input("Enter a number to check : "))    
if num == sum_cube(num):
    print("Entered number is Armstrong")
else:
    print("Entered number is Not Armstrong")