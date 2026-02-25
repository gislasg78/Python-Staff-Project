def get_prime_factors(number):
	factors = list()
	divisor = 2

	while (divisor <= number):
		if (number % divisor):
			divisor += 1
		else:
			factors.append(divisor)
			number /= divisor

	return factors


print("Decomposition of a number into its prime factors.")

try:
	number = int(input("Enter an integer value to decompose: "))

	if number < 0:
		raise Exception("Negative numbers cannot be entered.")
	elif number > 0:
		list_of_factors = get_prime_factors(number)

		print("")
		print(f"Number to be decomposed: [{number}].")
		print("Number of prime factors: [{}].".format(len(list_of_factors)))
		print(f"List of prime factors:")
		print("{}.".format(list_of_factors))
	else:
		print("There are no prime factors for the number zero.")

except Exception as e:
	print(e)
