# turtle module documentaion https://docs.python.org/3/library/turtle.html
# Tk colors / tkinter : python interface https://cs111.wellesley.edu/reference/colors
# python libraries @ https://pypi.org/


from turtle import Turtle, Screen

ninja = Turtle()
ninja.color("red")
ninja.shape("turtle")

# # drawing a square shape
# for step in range(4):
#     ninja.forward(100)
#     ninja.right(90)


# # drawing a circle shape
# for step in range(0, 360):
#     ninja.forward(1)
#     ninja.right(1)


#drawing a dashed line
for step in range (10):
    ninja.forward(10)
    ninja.penup()
    ninja.forward(10)
    ninja.pendown()

window = Screen()
window.exitonclick()