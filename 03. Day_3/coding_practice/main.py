print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age?"))

if height > 120:
    print("Can ride!")
    if age < 12:
        print("You have to pay $5 ticket")
    elif age <= 18:
        print("You have to pay $7 ticket")
    else:
        print("You have to pay $12 ticket")

else:
    print("Can't ride!")


a = int(input("Input an integer: "))
b = int(input("Input an integer: "))

integer_division = a // b
float_division = a / b

print(integer_division)
print(float_division)

year = int(input("Please enter a year: "))

if (year % 4 ) == 0:
    print("Leap year.")
else:
    print("Not leap year.")

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
sum = num1 + num2

if sum == 10:
    print("Sum is equal to 10")
else:
    print(f"Sum is not eyear = int(input('Which year do you want to check?'))")


year = int(input("Which year do you want to check? "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")



print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 3


print(f"Your final bill is: ${bill}")


n = int(input("Enter a digit"))

if (n % 2) != 0:
    print("Weird")

if (n % 2) == 0:
    if n > 20:
        print("Not Weird")
    elif n >= 6:
        print("Weird")
    elif n >= 2:
        print("Not Weird")


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age?"))

if height > 120:
    print("Can ride!")
    if age < 12:
        ticket_price = 5
        print(f"Child tickets are ${ticket_price}.")
    elif age <= 18:
        ticket_price = 7
        print(f"Youth tickets are ${ticket_price}.")
    else:
        if age >= 45 and age <= 55:
            ticket_price = 0
        else:
            ticket_price = 12

        print(f"Adult tickets are ${ticket_price}.")

    ans = input("Do you want a photo taken. Y or N? ")
    total_bill = 0
    if ans == "Y":
        total_bill = 3 + ticket_price
        print(f"Your final bill is ${total_bill}")
    if ans == "N":
        total_bill = ticket_price
        print(f"Your final bill is ${total_bill}")

else:
    print("Can't ride!")




