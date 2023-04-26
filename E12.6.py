import turtle as t

t.hideturtle()
t.pencolor('black')
t.fillcolor('red')
t.speed(500)

k = 1

t.begin_fill()
for x in range(5):
    t.forward(10 * k)
    t.right(90)
t.end_fill()

t.penup()
t.tracer(0)

count = 0
canvas = t.getcanvas()
for x in range(-10, 15):
    for y in range(-10, 15):
        # t.goto(x * k, y * k)
        # t.dot(5)
        s = canvas.find_overlapping(x, y, x, y)
        if len(s) == 1:
            count += 1

print(count)
t.done()
