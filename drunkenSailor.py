# Imports
from random import choice
from turtle import forward, left, mainloop, right, speed, backward

# Coinflip f(x)
def coinflip():
     return choice([-1, 1])

# Base Level Line Setup
def makeGraph(n):
     speed(1000)
     forward(1000)
     backward(1360)
     speed(n)

# Drunken walk
def drunkenWalk(n):
     for i in range(n):
          drinkEffect = coinflip()
          forward(10)
          left(drinkEffect * 90)
          forward(10)
          right(drinkEffect * 90)

# Execution
makeGraph(4)
drunkenWalk(71)
mainloop()