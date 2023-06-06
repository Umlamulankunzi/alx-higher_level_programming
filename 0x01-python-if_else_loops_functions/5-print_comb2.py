#!/usr/bin/python3
for val in range(100):
	if val == 99:
		print("{val:02d}".format(val=val))
	else:
		print("{val:02d}".format(val=val), end=", ")
