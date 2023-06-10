programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}
number = 99
code = 101
marks_of_subject = {
    93: "English",
    "Math": 99,
    88: 138,
    35.90: 46.20,
    number: code,
}

print(marks_of_subject[93])
print(marks_of_subject["Math"])
print(marks_of_subject[88])
print(marks_of_subject[35.90])
print(marks_of_subject[number])

marks = {
    "English": 88,
    "Math": 95,
}
marks["Bengali"] = 99
print(marks)

marks = {}
print(marks)
marks["Bengali"] = 91
print(marks)

for key in marks:
    print(key)
    print(marks[key])

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

capitals["Paris"] = 4
print(capitals)

# Nesting list in a dictionary

travel_log = {
    "Bangladesh": {"cities_visited": ["Dhaka", "Mymensigh", "Chittagong"], "total_visit": 12},
}

print(travel_log)

my_travel_history = {
    "Bangladesh": {"visited_cities": [{"Dhaka": 13}, {"Chittagong": 3}, {"Sylhet": 2}]},
}

print(my_travel_history)

my_visited_places = [
    {"city": "Dhaka",
     "visited_places": ["Uttara", "Banani", "Mirpur"],
     "total_visits": 150,
     },
    {"city": "Chittagong",
     "visited_places": ["Agrabad", "Potenga"],
     "total_visits": 6,
     },
]
print(my_visited_places[1]["total_visits"])

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(order["main"][2][0])

sum_list = [88, 90, 11]
sum = 90
position = 0
if sum in sum_list:
    position = sum_list.index(sum)

print(position)
