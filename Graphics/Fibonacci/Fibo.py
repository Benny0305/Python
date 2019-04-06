import turtle


value = 0
steps = 10000000
turtle.speed(10)

while steps > 0 :
    value = value + (value + 1)
    turtle.forward(value)
    turtle.left(1000)
    value += 0.0000001