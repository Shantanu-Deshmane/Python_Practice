def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
# print("GCD of entered numbers is : ",gcd(54,12))