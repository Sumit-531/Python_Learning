import random
import my_module

random_integer = random.randint(1, 3)
print(random_integer)

print(my_module.pi)
print(my_module.name)


random_float = random.random()
print(random_float)

print(random_float * 2)

print(random.random()*2)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
print(names)

name = input("What is your name?")
name_split = name.split("a")
print(name_split)

states_of_america = ["Alabama","Arizona","Alaska", "Arkansas", "California", "Colorado"]
print(len(states_of_america))
print(states_of_america[5])
states_of_america[0] = "Nevada"
print(states_of_america[0])

# Nested List
fruits = ["Strawberries", "Mangoes", "Lichies"]
vegetables = ["Potates", 'peas', "Carrots"]
dirty_six = [fruits,vegetables]
print(dirty_six)
print(dirty_six[0])
print(dirty_six[1])
print(dirty_six[1][2])
print(dirty_six[0][1])










