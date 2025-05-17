from turtle import *
tracer(0)
screensize(5000, 5000)
r = 20

for i in range(2):
    fd(28 * r); rt(90); fd(18 * r); rt(90)
up()
fd(14 * r); rt(90); fd(10 * r; lt(90)
down()
for i in range(2):
    fd(30 * r); rt(90); fd(7 * r); rt(90)
up()

for x in range(-99, 99):
    for y in range(-99, 99):
        goto(x * r, y * r)
        dot(3, "red")
update()

# (29 * 19 + 31 * 8) - (15 * 8)
