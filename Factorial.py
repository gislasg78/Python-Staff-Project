import sys

def factorial(number):
	if number <= 1:
		return 1
	else:
		return number * factorial(number - 1)


print("Obtaining the factorial of a number.")

try:
	number = int(input("Enter an integer: "))

	if number > 0:
		factorial_num = factorial(number)

		print()
		print("Results.")
		print(f"+ Number\t: [{number}].")
		print(f"+ Factorial\t: [{factorial_num}].")
		print(f"+ Recursions\t: [{sys.getrecursionlimit()}].")
	elif number < 0:
		raise Exception("Negative numbers should not be entered.")

except Exception as e:
	print()
	print(e)
else:
	print()
	print("The operation was a complete success.")
finally:
	print("The program has finished its execution.")
