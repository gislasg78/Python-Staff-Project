import sys

class Exception_Negative_Numbers(Exception):
	def __init__(self, message):
		self.message = message

	def __str__(self):
		return f"Exception for Negative Numbers: [{self.message}]."

def factorial(number):
	if number <= 1:
		return 1
	else:
		return number * factorial(number - 1)


print("Obtaining the factorial of a number.")

try:
	number = int(input("Enter an integer: "))
	factorial_number = factorial(number)

	if number > 0:
		print()
		print("Results.")
		print(f"+ Number\t: [{number}].")
		print(f"+ Factorial\t: [{factorial_number}].")
		print(f"+ Recursions\t: [{sys.getrecursionlimit()}].")
	elif number < 0:
		raise Exception_Negative_Numbers("Negative numbers should not be entered")
	else:
		raise Exception(f"The factorial for the number: [{number}] will always be: [{factorial_number}].")

except Exception as e:
	print()
	print(e)
else:
	print()
	print("The operation was a complete success.")
finally:
	print("The program has finished its execution.")
