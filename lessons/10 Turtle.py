# Import
from turtle import forward, mainloop, right, speed
from math import pi, sin

#speed(130)

## Square
def square():
     for i in range(4):
          forward(100)
          right(90)

## Polygon
def polygon(n, r):
     for i in range(n):
          forward(2 * r * sin(pi/n))
          right(360/n)

polygon(1, 40)
polygon(2, 40)
polygon(3, 40)
polygon(4, 40)
polygon(5, 40)
polygon(6, 40)
polygon(7, 40)
mainloop()