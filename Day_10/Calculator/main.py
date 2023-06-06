# calculator
from art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def sub(n1, n2):
    return n1 - n2


# Multiply
def mul(n1, n2):
    return n1 * n2


# divide
def div(n1, n2):
    return n1 / n2


def exponent(n1, n2):
    return n1 ** n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "^": exponent,
}
print(logo)


def calculator():
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        next_number = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, next_number)
        print(f"{num1} {operation_symbol} {next_number} = {answer}\n\n")

        decision = input(f"Type 'y' to continue with {answer}, or type 'n' to start again, or 'e' to exit.:").lower()
        if decision == "y":
            num1 = answer
        elif decision == "n":
            should_continue = False
            calculator()
        elif decision == "e":
            should_continue = False


calculator()


