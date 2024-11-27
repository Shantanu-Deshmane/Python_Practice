class calculateGCD:
    def __init__(self, num1,num2):
        self.num1=num1
        self.num2=num2
    
    def gcd(self):
        a=self.num1
        b=self.num2
        while a!=b:
            if a>b:
                a-=b
            else:
                b-=a
        return b

a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))
obj=calculateGCD(a,b)
result=obj.gcd()
print("GCD of Entered number is : ", result)