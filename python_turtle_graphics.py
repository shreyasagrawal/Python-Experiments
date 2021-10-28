#Author- Shreyas Agrawal
#Date- 9th Aug 2018

import turtle
bob= turtle.Turtle()

bob.pu()
bob.bk(300)
bob.pd()

def polygon(t, length, n):
    angle= 360 / n
    for i in range(n):        
        bob.fd(length)
        bob.rt(angle)
        bob.bk(length)
        bob.rt(angle)
        bob.end_fill()

polygon(bob, 80, 7)

bob.color(1, 0, 0)
bob.pu()
bob.fd (100)
bob.pd()
bob.end_fill()
polygon(bob, 80, 9)

bob.color(0, 1, 0)
bob.pu()
bob.fd (100)
bob.pd()
bob.end_fill()
polygon(bob, 80, 13)

bob.color(1, 0, 1)
bob.pu()
bob.fd (100)
bob.pd()
bob.end_fill()
polygon(bob, 80, 19)

bob.color(1, 1, 0)
bob.pu()
bob.fd (100)
bob.pd()
bob.end_fill()
polygon(bob, 80, 27)

bob.color(0, 0, 1)
bob.pu()
bob.fd (100)
bob.pd()
bob.end_fill()
polygon(bob, 80, 35)

bob.pu()
bob.fd(100)
bob.pd()

turtle.mainloop()
