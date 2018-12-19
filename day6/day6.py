#/usr/bin/python

import re

## Part 1

# Popualte the grid

x = 0
y = 0

grid = {}

while y <= 999:
	x = 0
	while x <= 999:
		grid[x,y] = 'off'
		x += 1
	y += 1


def get_instruction(string):
	instruction = re.search('toggle|turn on|turn off', string)
	return instruction.group(0)


def get_coordinates(string):
	p = re.compile(r'\d+')
	coordinates = p.findall(string)
	return coordinates


def switch_lights(x1,y1,x2,y2,instruction):
	if instruction == 'toggle':
		if grid[x1,y1] == 'off':
			grid[x1,y1] = 'on'
		else:
			grid[x1,y1] = 'off'
	elif instruction == 'turn on':		
		grid[x1,y1] = 'on'
	elif instruction == 'turn off':
		grid[x1,y1] = 'off'


def navigate_grid(x1,y1,x2,y2,instruction):
	x_axis=x2-x1
	y_axis=y2-y1

	while x1 <= x_axis:
		while y1 <= y_axis:
			print 'x1: {0}'.format(x1)
			print 'y1: {0}'.format(y1)
			print 'x2: {0}'.format(x2)
			print 'y2: {0}'.format(y2)
			switch_lights(x1,y1,x2,y2,instruction)
			y1+=1
		x1+=1


with open('day6_test.txt', 'r') as file:
  for row in file:
    string = row.strip()
   
    coordinates = get_coordinates(string)
    x1 = int(coordinates[0])
    y1 = int(coordinates[1])
    x2 = int(coordinates[2])
    y2 = int(coordinates[3])

    instruction = get_instruction(string)

    navigate_grid(x1,y1,x2,y2,instruction)


lights_on=0

for x, y in grid:
	if grid[x,y] == 'on':
		lights_on += 1

print 'The number of lights on is: {0}'.format(lights_on)
