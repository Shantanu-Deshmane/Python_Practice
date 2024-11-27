def primeNum(num):
    if num <= 1:
        return ("Entered num is not prime")

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return ("Entered num is not prime")
    return ("Entered num is Prime")