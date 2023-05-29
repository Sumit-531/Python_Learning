import random
# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!\nPasswords at least 14 to 16 characters are better!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# for letters
letters_range = nr_letters + 1
letter_string = ""
for n in range(1, letters_range):
    random_letter = (random.choice(letters))
    letter_string += (random_letter + " ")

# for numbers
numbers_range = nr_numbers + 1
number_string = ""
for n in range(1, numbers_range):
    random_number = (random.choice(numbers))
    # number_string += random_number
    number_string += (random_number + " ")


# for symbols
symbols_range = nr_symbols + 1
symbols_string = ""
for n in range(1, symbols_range):
    random_symbol = (random.choice(symbols))
    symbols_string += (random_symbol + " ")

password = letter_string + symbols_string + number_string

# split function splits a string into a list
pass_list = password.split()
# shuffling the item in the list
random.shuffle(pass_list)

pass_list_string = ""
for n in pass_list:
    pass_list_string += n

print(f"Here is your password: {pass_list_string}")
