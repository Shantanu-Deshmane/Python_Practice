class calculate:
    def __init__(self, num1):
        self.num1=num1

    def calculate_sum(self):
        a=self.num1
        sum=0
        product=1
        for i in a:
            sum+=int(i)
            product*=int(i)
            
        
        return sum, product
a=input("Enter a number: ")
obj=calculate(a)
result=obj.calculate_sum()

print("Sum and product is: ", result)
