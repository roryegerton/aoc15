#!/usr/bin/python

from array import *

directions=[]
with open('day3_input.txt', 'r') as file:
  for line in file:
    for direction in line:
    	directions.append(direction)


up = '^'
down = 'v'
left = '<'
right = '>'



## Part 1

house1 = {}

x=0
y=0

house1[x,y]=1

for direction in directions:

	if direction == up:
		y+=1	
		
	elif direction == down:
		y-=1		
		
	elif direction == left:
		x-=1
		
	elif direction == right:
		x+=1
		
	if not house1.has_key((x,y)):
		house1[x,y] = 0
	
	house1[x,y] = house1[x,y] + 1

print 'The number of houses is: {0}'.format(len(house1))


## Part 2

house2 = {}

x1=0
y1=0
x2=0
y2=0

house2[x1,y1] = 2

first_turn = True
second_turn = False

for direction in directions:

	if first_turn:
		# first route
		if direction == up:
			y1+=1			
		elif direction == down:
			y1-=1		
		elif direction == left:
			x1-=1
		elif direction == right:
			x1+=1
		if not house2.has_key((x1,y1)):
			house2[x1,y1] = 0

		house2[x1,y1] = house2[x1,y1] + 1


	if second_turn:
		# first route
		if direction == up:
			y2+=1			
		elif direction == down:
			y2-=1		
		elif direction == left:
			x2-=1
		elif direction == right:
			x2+=1
		if not house2.has_key((x2,y2)):
			house2[x2,y2] = 0

		house2[x2,y2] = house2[x2,y2] + 1

		second_turn = False


	if first_turn == True:
		first_turn = False
		second_turn = True
	else:
		first_turn = True


print 'The number of houses is: {0}'.format(len(house2))

