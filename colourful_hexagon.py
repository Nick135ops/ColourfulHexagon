import turtle

draw = turtle.Turtle()
wn = turtle.Screen()
draw.speed(90)
wn.bgcolor('black')
colors = ['red', 'green', 'blue', 'purple', 'orange', 'yellow']

for x in range(360):
    draw.pencolor(colors[x % 6])
    draw.width(x / 100 + 1)
    draw.forward(x)
    draw.left(59)
turtle.done()
