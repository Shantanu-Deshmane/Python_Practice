a = int(input("enter a year : "))
if((a % 400 == 0) or  (a % 100 != 0) and (a % 4 == 0)):   
    print("Entered year is leap")
else:
    print("Entered year is non-leap year")

