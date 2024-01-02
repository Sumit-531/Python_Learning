# import turtle
# timmy = turtle.Turtle()
#
#
# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.shapesize(5.0, 5.0, 3.0)
# # timmy.forward(100.0)
# timmy.fd(100.0)
# timmy.color("red", "green")
#
#
# def new_turtle():
#     atu = Turtle()
#     atu.shape("turtle")
#     atu.shapesize(2.0, 2.0, 1.0)
#     atu.color("coral")
#     atu.backward(30.0)
#
#
# new_turtle()
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()



# import prettytable

from prettytable import PrettyTable


table = PrettyTable()

# table.valign = 't'
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
