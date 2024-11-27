def armstrong(n):
        length=len(str(n))
        sum=0
        temp=n
        while temp>0:
            a=temp%10
            sum+=a**length
            temp//=10
        if sum == n:
            return "Entered number is Armstrong"
        else:
             return "Entered number is Not Armstrong"