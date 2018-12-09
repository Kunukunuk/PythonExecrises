#!/bin/python3

from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(15):
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  for dash in range(10):
      forward(10)
      penup()
      forward(10)
      pendown()
  #forward(150)
  penup()
  backward(210)
  left(90)
  forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160,110)
ada.pendown()

bob = Turtle()
bob.color('yellow')
bob.shape('turtle')

bob.penup()
bob.goto(-160,90)
bob.pendown()

john = Turtle()
john.color('blue')
john.shape('turtle')

john.penup()
john.goto(-160,70)
john.pendown()

will = Turtle()
will.color('green')
will.shape('turtle')

will.penup()
will.goto(-160,50)
will.pendown()

for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  john.forward(randint(1,5))
  will.forward(randint(1,5))
  
