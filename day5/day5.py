#/usr/bin/python


## PART 1

nice1 = 0

def two_in_a_row(string):
	allowed = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

	for letter in allowed:
		if letter*2 in string:
			return True

def three_vowels(string):
	counter = 0
	vowels = ['a','e','i','o','u']

	for char in string:
		if char in vowels:
			counter += 1

	return counter

def disallowed_two_in_a_row(string):
	disallowed = ['ab','cd','pq','xy']

	for couple in disallowed:
		if couple in string:
			return True


with open('day5_input.txt', 'r') as file:
  for row in file:
    string = row.strip()

    vowel_count = three_vowels(string)
    allowed = two_in_a_row(string)
    disallowed = disallowed_two_in_a_row(string)

    if ((allowed == True) and (vowel_count >= 3)) and (disallowed != True):
    	nice1 += 1


print 'The number of nice strings is: {0}'.format(nice1)




## PART 2

nice2 = 0

def a_pair_appear_twice(string):
	
	index = 0
	str_len = len(string)

	while index <= str_len:
		two_char_str = string[index:index+2]
		two_char_len = len(two_char_str)
		str_occur = string.count(two_char_str)

		if str_occur >= 2 and two_char_len == 2:
			return True

		index += 1

	return False


def a_repeating_letter(string):

	index = 0
	str_len = len(string)

	while index <= str_len:
		if index+2 < str_len:
			if string[index] == string[index+2]:
				return True

		index += 1

	return False


with open('day5_input.txt', 'r') as file:
	for row in file:
		string = row.strip()

		appears_twice = a_pair_appear_twice(string)
		repeat_letter = a_repeating_letter(string)

		if appears_twice and repeat_letter:
			nice2 += 1

print 'The number of nice strings is: {0}'.format(nice2)
