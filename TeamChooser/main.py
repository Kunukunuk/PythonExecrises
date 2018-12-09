#!/bin/python3

from random import choice

players = []
file = open('players.txt', 'r')
players = file.read().splitlines()

file = open('teamnames.txt', 'r')

teamNames = []
teamNames = file.read().splitlines()

teamAName = choice(teamNames)
print(teamAName)
teamNames.remove(teamAName)
teamBName = choice(teamNames)
teamNames.remove(teamBName)
teamA = []
teamB = []

while len(players) > 0:
  playerA = choice(players)
  teamA.append(playerA)
  players.remove(playerA)
  print('Players left: ', players)
  
  if players == []:
    break
  
  playerB = choice(players)
  teamB.append(playerB)
  players.remove(playerB)
  print('Players left: ', players)

print('Team ', teamAName, ': ', teamA)
print('Team ', teamBName, ': ', teamB)