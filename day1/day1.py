#!/usr/bin/python

# Variables

moves= []

class Building():

	def __init__(self, start=0, pos=1):
		self.floor = start
		self.position = pos

# Read file and return all moves
with open('day1_input.txt', 'r') as file:
  for line in file:
    for move in line:
    	moves.append(move)


# PART 1

build1 = Building()

for move in moves:
	if move == '(':
		build1.floor += 1
	elif move == ')':
		build1.floor -= 1

print 'The correct floor is: {0}'.format(build1.floor)


# PART 2

build2 = Building()

for move in moves:
	if move == '(':
		build2.floor += 1
	elif move == ')':
		build2.floor -= 1

	if build2.floor == -1:
		break
	else:
		build2.position += 1


print 'The position when we reach the basement is: {0}'.format(build2.position)




