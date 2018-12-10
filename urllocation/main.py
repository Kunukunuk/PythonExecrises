#!/bin/python3

import json
import turtle
import urllib.request
import time

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
long = location['longitude']
lat = location['latitude']
print(result)

screen = turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.jpg')

screen.register_shape('iss.png')
iss = turtle.Turtle()
iss.shape('iss.png')
iss.setheading(90)

iss.penup()
iss.goto(long, lat)

issLocation = turtle.Turtle()
issLocation.penup()
issLocation.color('yellow')
issLocation.goto(long, lat)
issLocation.dot(5)
issLocation.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=29.55&lon=95.1'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

over = result['response'][1]['risetime']

style = ('Arial', 6, 'bold')
issLocation.write(time.ctime(over), font=style)