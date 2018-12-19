#!/usr/bin/python

import re
import md5



## PART 1

counter = 0
regex = re.compile('^00000\d*')

while counter >= 0:

	ad_coin = md5.new('iwrupvqb{0}'.format(counter)).hexdigest()

	if regex.match(ad_coin):
		print counter
		break

	counter += 1



## PART 2

counter = 0
regex = re.compile('^000000\d*')

while counter >= 0:

	ad_coin = md5.new('iwrupvqb{0}'.format(counter)).hexdigest()

	if regex.match(ad_coin):
		print counter
		print ad_coin
		break

	counter += 1