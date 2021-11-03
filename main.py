import random
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(198, 12, 12), (39, 76, 76), (38, 217, 217), (238, 227, 227), (229, 159, 159), (27, 40, 40), (215, 74, 74), (15, 154, 154), (199, 14, 14), (242, 246, 246), (243, 33, 33), (229, 17, 17), (73, 9, 9), (60, 14, 14), (224, 141, 141), (10, 97, 97), (221, 160, 160), (17, 18, 18), (46, 214, 214), (11, 227, 227), (81, 73, 73), (238, 156, 156), (74, 213, 213), (77, 234, 234), (52, 234, 234), (3, 67, 67)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):

    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0 :
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()