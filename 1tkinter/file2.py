def get_numbers():
    numbers = []
    for i in range(10):
        while True:
            try:
                num = int(input(f"Enter number {i+1} of 10: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    return numbers

def write_to_file(filename, numbers):
    with open(filename, 'w') as file:
        for num in numbers:
            file.write(str(num) + '\n')

def separate_numbers_and_write():
    numbers = get_numbers()  
    write_to_file('1tkinter/ALLNUM.txt', numbers) 
    
    odd_numbers = [num for num in numbers if num % 2 != 0]  
    even_numbers = [num for num in numbers if num % 2 == 0] 

    write_to_file('1tkinter/ODD.txt', odd_numbers)  
    write_to_file('1tkinter/EVEN.txt', even_numbers) 
    
    print("Numbers have been successfully written to 'ALLNUM.txt', 'ODD.txt', and 'EVEN.txt'.")
separate_numbers_and_write()
