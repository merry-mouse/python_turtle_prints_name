import turtle

name = input("Please enter your name:\n")

turtle.color('green')
style = ('Courier', 90, 'normal')
turtle.write(name, font=style, align='center')
turtle.hideturtle()

turtle.done()

