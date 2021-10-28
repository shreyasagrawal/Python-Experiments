import turtle
bob= turtle.Turtle ()

def polygon(t, length, n):
    angle= 360 / n
    for i in range(n):
        bob.fd(length)
        bob.lt(angle)

polygon(bob, 80, 9)


import math
def circle(t, r):
    circumference= 2 * math.pi * r
    n=50
    length = circumference / n
    polygon (t, length, n)


circle(bob, 80)


turtle.mainloop()



