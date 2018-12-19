#!/usr/bin/python


class Present():

	def __init__(self, start=0):
		self.area = start



def split_str(dims):
	split_dims = dims.split('x')
	return split_dims

def get_length(dims):
	split_dims = split_str(dims)
	return int(split_dims[0])

def get_width(dims):
	split_dims = split_str(dims)
	return int(split_dims[1])

def get_height(dims):
	split_dims = split_str(dims)
	return int(split_dims[2])


## Read in all dimensions

dimensions =[]
with open('day2_input.txt', 'r') as file:
  for dimension in file:
    dimensions.append(dimension.strip())


## Part 1

present1 = Present()

for dimension in dimensions:
	l = get_length(dimension)
	w = get_width(dimension)
	h = get_height(dimension)

	top_bottom = l*w
	sides = l*h
	ends = h*w

	smallest_area = sorted([top_bottom, sides, ends])[0]

	present1.area += ((top_bottom*2) + (sides*2) + (ends*2) + smallest_area)


print "PART 1: The total area of paper is: {0}".format(present1.area)



## Part 2

present2 = Present()

for dimension in dimensions:
	l = get_length(dimension)
	w = get_width(dimension)
	h = get_height(dimension)

	short1 = sorted([l, w, h])[0]
	short2 = sorted([l, w, h])[1]

	volume = l * w * h

	present2.area += ((short1*2) + (short2*2) + volume)


print "PART 2: The total ribbon length is: {0}".format(present2.area)