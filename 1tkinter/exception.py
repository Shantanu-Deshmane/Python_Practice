def divide_numbers():
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        result = num1 / num2
        
    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")
    except ValueError:
        print("Error! Please enter valid numbers.")
    else:
        print(f"The result of dividing {num1} by {num2} is: {result}")
    finally:
        print("Division operation attempted.")

divide_numbers()
