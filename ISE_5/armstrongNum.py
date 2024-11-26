num=int(input("Enter any number: "))
sum=0
temp=num
while temp>0:
    a=temp%10
    sum+=a**3
    temp//=10

if num == sum:
    print(f"{num} is Armstrong Number.")
else:
    print(f"{num} is Not Armstrong Number.")

