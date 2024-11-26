class factorial:
    def __init__(self, num):
        self.num=num
    
    def calculate_fact(self):
        a=self.num
        fact=1
        for i in range(1,a+1):
            fact*=i
        return fact
a=int(input("Enter a number : "))
obj=factorial(a)
result=obj.calculate_fact()
print("Factorial of entered number: ",result)