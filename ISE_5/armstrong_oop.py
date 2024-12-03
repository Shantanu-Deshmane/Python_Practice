class calculateArmstrong:
    def __init__(self,num):
        self.num=num

    def armstrong(self):
        n=self.num
        length=len(str(n))
        sum=0
        temp=n
        while temp>0:
            a=temp%10
            sum+=a**length
            temp//=10
        return (sum)

num=int(input("Enter a number to find Armstrong: "))
obj=calculateArmstrong(num) 
result=obj.armstrong()         
if result == num:
    print("Entered number is Armstrong")
else:
    print("Entered number is Not Armstrong")


        