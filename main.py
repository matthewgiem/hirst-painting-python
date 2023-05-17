import turtle
import random
# import colorgram

# # import hirst colors only needs to be done once *I removed the first two colors as they were shades of white
# colors = colorgram.extract('hirst.jpg', 27)
# rgb_colors = []
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

hirst_colors = [(199, 175, 117), (212, 222, 215), (125, 36, 24), (223, 224, 228), (167, 106, 56), (186, 159, 52),
                (6, 57, 83), (108, 68, 85), (112, 161, 175), (21, 122, 174), (63, 153, 138), (39, 36, 35), (76, 40, 48),
                (9, 68, 47), (90, 141, 52), (182, 96, 79), (131, 38, 41), (141, 171, 156), (210, 200, 149),
                (179, 201, 186), (173, 153, 159), (212, 183, 176), (151, 114, 119), (177, 198, 203), (206, 184, 190)]


tim = turtle.Turtle()
turtle.colormode(255)
tim.penup()
tim.hideturtle()
tim.speed("fastest")

for x in range(25):
    if x % 5 == 0 and x != 0:
        if x % 2 != 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(50)
        elif x % 2 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(0)
            tim.forward(50)
    tim.dot(20, random.choice(hirst_colors))
    tim.forward(50)


screen = turtle.Screen()
screen.exitonclick()
