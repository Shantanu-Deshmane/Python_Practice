num = int(input("Enter a number: "))
if num <= 1:
    print("Entered num is not prime")
else:
    i = 2
    while i <= int(num**0.5):
        if num % i == 0:
            print("Entered num is not prime")
            break 
        i += 1
    else:
        print("Entered num is Prime")
