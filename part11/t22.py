from turtle import *
import random

color_list = ["blue", "red", "yellow", "purple"]
screensize(500, 500,"black")
for i in range(10):
    color(random.choice(color_list))
    penup()
    goto(0, -(i+1)*10)
    pendown()
    circle((i+1)*10)
mainloop()
