# Program that reads the command line and records it in a plain text output file.
# How to invoke this program:
# 	python3 Example.py 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

import sys

# Preliminary initialization of variables
my_prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
total = 0
del(sys.argv[0])	# The first one is deleted because it has the program name that was executed.

print("Command Line Argument Reader.")
print(f"Number of parameters: [{len(sys.argv)}].")

# Branching by deciding whether or not there are arguments on the command line.
print()
if sys.argv:
	file = open("example.txt", "a")
	print("List of command-line parameters.")

	for arg in sys.argv:
		print(f"[{arg}].", end='\t')
		file.write(f"[{arg}].\n")

		try:
			total += int(arg)
		except Exception as e:
			print()
			print("An error has occurred. Only numbers can be provided.")
			print(e)

	print(f"\n\nTotal: [{total}].")

	file.write(f"[{total}].\n")
	file.close()
else:
	file = open("example.txt", "a")
	print("List of preset and default parameters.")

	for item in my_prime_list:
		print(f"[{item}].", end='\t')
		file.write(f"[{item}].\n")
		total += item

	print(f"\n\nTotal: [{total}].")
	file.write(f"[{total}].\n")
	file.close()

# Retrieving and viewing the contents of the output file.
file = open("example.txt", "r")
lines = file.readlines()

print()
print("Content recorded in the output file.")
print(f"\n{lines}\n")

file.close()
