# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
upper_range = len(word_list) - 1
rand_number = random.randint(0, upper_range)
chosen_word = (word_list[rand_number])

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = (input("Guess a letter: ")).lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for n in chosen_word:
    if n == guess:
        print("Wright")
    else:
        print("Wrong")




