class gcd_calculate:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def GCD(self):
        a,b=self.num1,self.num2
        while a!=b:
            if a>b:
               a-=b
            else:
                b-=a
        return a

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

gcdCalculate=gcd_calculate(a,b)
gcd=gcdCalculate.GCD()

print("GCD of Entetred data is: ",gcd)


        