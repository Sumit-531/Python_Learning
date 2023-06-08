# importing the logo
from art import logo

# random
import random


def black_jack():
    user_card = []
    computer_card = []
    score = 0

    # card deck
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # for first two card of user
    for _ in range(2):
        card = random.choice(deck)
        user_card.append(card)
    for n in user_card:
        score += n

    # computer card
    computers_choice = random.choice(deck)
    computer_card.append(computers_choice)
    current_score = 0
    computer_final_score = 0
    # player decision for playing the game
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
    if play == "n":
        print("Invalid input")
    elif play == "y":
        print(logo)
        print(f"Your cards: {user_card}, current score: {score}")
        print(f"Computer's first card: {computer_card}")
        # flag
        should_continue = True
        while should_continue:
            decision = input("Type 'y' to get another card, type 'n' to pass:").lower()
            if decision == "y":
                card2 = random.choice(deck)
                user_card.append(card2)
                for n in user_card:
                    current_score += n

                print(f"Your cards: {user_card}, current score:  {current_score}")
                print(f"Computer's first card: {computer_card}")

                # computer
                for _ in range(2):
                    computer_final_hand = random.choice(deck)
                    computer_card.append(computer_final_hand)
                for n in computer_card:
                    computer_final_score += n

                print(f"Your final hand: {user_card}, final score: {current_score}")
                print(f"Computer's final hand: {computer_card}, final score: {computer_final_score}")

                if (current_score > computer_final_score) and (current_score <= 21):
                    print("You win")

                elif (current_score > 21):
                    print("You went over. Computer win.")

                elif (computer_final_score > current_score) and (computer_final_score <= 21):
                    print("You lose")
                elif (computer_final_score > 21):
                    print("Opponent went over. You win")

                should_continue = False
                black_jack()
            elif decision == "n":
                for _ in range(2):
                    computer_final_hand = random.choice(deck)
                    computer_card.append(computer_final_hand)
                for n in computer_card:
                    computer_final_score += n

                final_hand = user_card
                final_user_score = score
                print(f"final hand: {final_hand}, final score: {final_user_score}")
                print(f"Computer's final hand: {computer_card}, final score: {computer_final_score}")

                if (final_user_score > computer_final_score) and (final_user_score <= 21):
                    print("You win.")

                elif (computer_final_score > 21):
                    print("Opponent went over. You win")

                elif (computer_final_score > final_user_score) and (computer_final_score <= 21):
                    print("You lose")
                    should_continue = False

                black_jack()


black_jack()