import random
from art import logo


def random_generated_number():
    """This function generates a random number from 1 to 100"""
    number = random.randint(1, 100)
    return number


def decreasing_lives(lives):
    """This function decreases lives after every wrong attempts"""
    if lives >= 0:
        lives -= 1
        return lives


def assigning_lives(user_difficulty):
    """This function assigns lives as per difficulty"""
    if user_difficulty == "easy":
        lives_remain = 10
        return lives_remain
    elif user_difficulty == "hard":
        lives_remain = 5
        return lives_remain


def compare(answer, user_guess):
    """This funciton compares the random number with user guessed number and returns the verdict"""
    if user_guess > answer:
        return "Too high"
    elif user_guess < answer:
        return "Too low"
    else:
        return f"You got it! the answer was {answer}"


def number_guessing():
    print(logo)
    print("Welcome to the number guessing game!\nI am thinking a number between 1 to 100")
    real_number = random_generated_number()
    decision = input("Chose a difficulty. Type 'easy' or 'hard': ").lower()

    remaining_lives = assigning_lives(user_difficulty=decision)
    print(f"You have {remaining_lives} attempts to guess the number.")

    is_game_over = False

    while not is_game_over:

        if remaining_lives != 0:
            guess = int(input("Make a guess: "))
            print(compare(answer=real_number, user_guess=guess))
            if "You got it!" in (compare(answer=real_number, user_guess=guess)):
                is_game_over = True
            remaining_lives = decreasing_lives(remaining_lives)
            if "You got it!" not in (compare(answer=real_number, user_guess=guess)):
                print(f"You have {remaining_lives} attempts to guess the number.")



        elif remaining_lives == 0:
            print("Game over!")
            is_game_over = True

            print(f"The answer was {real_number}")


number_guessing()
playing_decision = input("Do you want to play the game again from the start? If yes type 'y' and for exit type 'n':")
if playing_decision == "y":

    number_guessing()
else:
    print("Thank you for playing.")

