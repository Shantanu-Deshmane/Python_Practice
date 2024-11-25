# creating a class
class gcd_calculate:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

# Created a function to calculate GCD
    def GCD(self):
        a,b=self.num1,self.num2
        while a!=b:
            if a>b:
               a-=b
            else:
                b-=a
        return a

# Taking input from user
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

# Creating a object named 'gcd' of class 'gcd_calculate'
gcd=gcd_calculate(a,b)
gcdCalculate=gcd.GCD()

print("GCD of Entetred data is: ",gcdCalculate)


        