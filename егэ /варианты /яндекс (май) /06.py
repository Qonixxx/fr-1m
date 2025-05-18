from turtle import *
tracer(0)
screensize(5000, 5000)
r = 20

rt(30)

for i in range(3): rt(45); fd(4 * r); rt(45)

rt(315); fd(4 * r)

for i in range(2): rt(90); fd(4 * r)

up()


for x in range(-99, 99):
    for y in range(-99, 99):
        goto(x * r, y * r)
        dot(3, "red")
update()
