#!/usr/bin/python3
for val in range(100):
	if val == 99:
		print("{val}".format(val=val))
	else:
		print("{val}".format(val=val), end=", ")
