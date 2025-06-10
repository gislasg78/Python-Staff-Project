def get_prime_factors(number):
	factors = list()
	divisor = 2

	while (divisor <= number):
		if (number % divisor) == 0:
			factors.append(divisor)
			number /= divisor
		else:
			divisor += 1

	return factors


print("Decomposition of a number into its prime factors.")

number = int(input("Enter an integer value to decompose: "))
list_of_factors = get_prime_factors(number)

print("")
print(f"Number to be decomposed:\t{number}.")
print(f"List of prime factors:\t\t{list_of_factors}.")
