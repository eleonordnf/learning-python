import turtle
t = turtle.Pen()
t.speed(0)
colors = ["dark blue", "blue", "violet", "pink"]
for x in range(100):
    t.pencolor( colors[ x % 4])
    t.forward(2*x)
    t.left(91)