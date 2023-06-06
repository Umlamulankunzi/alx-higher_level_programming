#!/usr/bin/python3
for val in range(100):
	print("{val}".format(val=val), end="")
	if val == 99:
		print()
	else:
		print(", ", end="")
