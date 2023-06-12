import random
import hangman_art
import hangman_word

print(hangman_art.logo)

upper_range = len(hangman_word.word_list) - 1
rand_number = random.randint(0, upper_range)
chosen_word = (hangman_word.word_list[rand_number])

lives = 6

length_of_chosen_word = len(chosen_word)
display = []
for _ in chosen_word:
    display += "_"

end_of_game = False
while not end_of_game:
    guess = (input("Guess a letter: ")).lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for n in range(length_of_chosen_word):
        letter = chosen_word[n]
        if letter == guess:
            display[n] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win!")
    if lives == 0:
        end_of_game = True
        print("You lose!")

    print(hangman_art.stages[lives])

print(f"The word was {chosen_word}")
