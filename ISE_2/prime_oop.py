class isPrime:
    def __init__(self,num):
        self.num=num
    
    def primeNum(self):
        num1=self.num
        if num1 <= 1:
            return ("Entered num is not prime")

        for i in range(2, int(num1**0.5) + 1):
            if num1 % i == 0:
                return ("Entered num is not prime")
        return ("Entered num is Prime")
    
num=int(input("Enter a number: "))
obj=isPrime(num)
result=obj.primeNum()
print(result)
        