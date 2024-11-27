def sum_cube(num):
    sum=0
    temp=num
    length=len(str(num))
    while temp>0:
        a=temp%10
        sum+=a**length
        temp//=10
    print(sum)
    return sum

num=int(input("Enter a number to check : "))    
if num == sum_cube(num):
    print("Entered number is Armstrong")
else:
    print("Entered number is Not Armstrong")
