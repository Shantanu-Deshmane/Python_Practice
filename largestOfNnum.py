a = int(input("How many numbers you want to enter? : "))
num_list=[]
for i in range(a):
    numbers = int(input(f"Enter number {i+1}: "))
    num_list.append(numbers)
    
print("Largest number of entered %d numbers is : "%a,max(num_list))