from art import logo
from art import vs
from game_data import data
from random import randint

score = 0


# random function to assign.
def random_choice():
    """This function randomly select a position in the data list"""
    upper_bound = len(data) - 1
    rand_position = randint(0, upper_bound)
    return rand_position


random_selection_one = random_choice()
random_selection_two = random_choice()


# get data from game data dictionary and assign them in a variable.
def candidate(m, n):
    """This function returns name, description and country of a candidate. Furthermore, returns follower."""
    name = data[m]['name']
    description = data[m]["description"]
    country = data[m]["country"]
    follower = data[m]["follower_count"]
    if n == "follower":
        return follower
    elif n == "data":
        return (f"{name}, a {description}, from {country}.")


candidate_one_data = candidate(m=random_selection_one, n="data")
candidate_one_follower = int(candidate(m=random_selection_one, n="follower"))

candidate_two_data = candidate(m=random_selection_two, n="data")
candidate_two_follower = int(candidate(m=random_selection_two, n="follower"))

is_game_over = False
while not is_game_over:

    print(logo)
    if random_selection_one != random_selection_two:
        print(f"Compare A: {candidate_one_data}")
        print(vs)
        print(f"Compare B: {candidate_two_data}")
    decision = input("Who has more followers: Type 'A' or 'B':").lower()

    if decision == "a":
        if candidate_one_follower > candidate_two_follower:
            score += 1
            print(score)
            candidate_one_data = candidate_one_data
            candidate_one_follower = candidate_one_follower
            random_selection_two = random_choice()
            candidate_two_data = candidate(m=random_selection_two, n="data")
            candidate_two_follower = int(candidate(m=random_selection_two, n="follower"))

        else:
            print(score)
            print("Game over!")
            is_game_over = True
    elif decision == "b":
        if candidate_two_follower > candidate_one_follower:
            score += 1
            print(score)
            candidate_one_data = candidate_two_data
            candidate_one_follower = candidate_two_follower
            random_selection_two = random_choice()
            candidate_two_data = candidate(m=random_selection_two, n="data")
            candidate_two_follower = int(candidate(m=random_selection_two, n="follower"))

        else:
            print(score)
            print("Game over!")
            is_game_over = True
