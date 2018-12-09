#!/bin/python3

import pygal

piechart = pygal.Pie()
piechart.title = "Pets"
piechart.add('Dog', 10)
piechart.add('Cat', 2)
piechart.add('Snake', 5)
piechart.render()

barChart = pygal.Bar()
barChart.title = "Pets From File"

fileInput = open('Pets.txt', 'r')
for line in fileInput.read().splitlines():
  if line:
    name, amount = line.split(' ')
    barChart.add(name, int(amount))
fileInput.close()

barChart.render()