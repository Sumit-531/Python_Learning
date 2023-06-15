import random


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


upper_range = int((len(names)) - 1)

decision = random.randint(0, upper_range)

print(f"{names[decision]} is going to buy the meal today!")