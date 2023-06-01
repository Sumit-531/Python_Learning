def greet():
    print("My name is Sumit Chakraborty")
    print(1 + 1)
    sum = 0
    for _ in range(5):
        sum += 1
    print(sum)


greet()


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Sumit")

# Function
# with more than one input

def greet_with(name, location):
    # print(f"Customer's name is: {name}")
    # print(f"Customer's location is: {location}")
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with(name="Sumit", location="Dhaka")


def number(a, b, c):
    print(f"Number 1: {a}")
    print(f"Number 2: {b}")
    print("Number 3: " + str(c))


number(a=1, c=9, b=36)

import math

print(math.ceil(7 / 6))


def prime_checker(number):
    is_prime = True
    for i in range(2, n):
        if (number % i == 0):
            is_prime = False

    if is_prime:
        print("It is a prime number.")
    elif (number == 1):
        print("It is not a prime number.")
    else:
        print("It is not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)


def even_odd_checker(number):
    if (number >= 1) and (number <= 88):
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")


n = int(input("Insert a number to check is it even or odd?(From 1 to 88) :\n"))
even_odd_checker(number=n)


def is_leap(year):
    leap = False

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap = True
        print("True")
    else:
        print("False")

    return leap


year = int(input())
is_leap(year)

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i ** 2)
