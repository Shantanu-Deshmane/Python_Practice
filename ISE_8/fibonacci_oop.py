class calculate_fibonacci:
    def __init__(self,limit):
        self.limit=limit

    def fibo(self):
        a=0
        b=1
        seq=[a,b]
        for i in range(2,limit1):
            c=a+b
            a,b=b,c
            seq.append(c)
        return seq

limit1=int(input("Enter a limit to print series up to : "))
obj=calculate_fibonacci(limit1)
fibonacci=obj.fibo()

print(fibonacci,end=" ")

            
        