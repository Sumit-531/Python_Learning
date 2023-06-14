################### Scope ####################

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()  # 2
print(f"enemies outside function: {enemies}")  # 1


def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()

number = 1


def cal():
    return number + 1


print(cal())

n = int(input())


def print_string():
    n_string = ""
    for x in range(1, n + 1):
        number = x
        number_string = str(number)
        n_string += number_string
    return n_string


print(print_string())

n = int(input())
word_list = []
for x in range(n):
    x = input("")
    word_list += x

print(word_list)
