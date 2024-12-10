# Function to count vowels, consonants, uppercase, lowercase, and other characters
def count_characters_in_file(filename):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    total_vowels = 0
    total_consonants = 0
    total_uppercase = 0
    total_lowercase = 0
    total_other = 0

    with open(filename, 'r') as file:
            content = file.read()
            
            for char in content:
                if char in vowels:
                    total_vowels += 1
                elif char in consonants:
                    total_consonants += 1
                else:
                    total_other += 1
            
            for char in content:
                if char.isupper():
                    total_uppercase += 1
                elif char.islower():
                    total_lowercase += 1
        
    print(f"Total Vowels in file: {total_vowels}")
    print(f"Total Consonants in file: {total_consonants}")
    print(f"Total Capital letters in file: {total_uppercase}")
    print(f"Total Small letters in file: {total_lowercase}")
    print(f"Total Other than letters: {total_other}")


filename = "1tkinter/sample.txt"
count_characters_in_file(filename)
