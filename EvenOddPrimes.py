def IsEven(number):
	return not(number % 2)

def IsOdd(number):
	return (number % 2)

def IsPrime(number):
	return (((number == 2) or (number == 3) or (number == 5) or (number == 7)) or
		((number % 2) and (number % 3) and (number % 5) and (number % 7)))

def extract_of_evens_odds_primes(numbers):
	return [sorted([x for x in numbers if IsEven(x)]),
		sorted([x for x in numbers if IsOdd(x)]),
		sorted([x for x in numbers if IsPrime(x)])]

def sum_of_evens_odds_primes(numbers):
	addition_evens, counter_evens = 0, 0
	addition_odds, counter_odds = 0, 0
	addition_primes, counter_primes = 0, 0

	for number in numbers:
		if (IsEven(number)):
			counter_evens += 1
			addition_evens += number

		if (IsOdd(number)):
			counter_odds += 1
			addition_odds += number

		if (IsPrime(number)):
			counter_primes += 1
			addition_primes += number

	return [[counter_evens, addition_evens],
		[counter_odds, addition_odds],
		[counter_primes, addition_primes]]

legends = [["Evens", "Odds", "Primes"], ["Count", "Sum"]]
numbers = set()

print("Counter for even, odd, and prime numbers.")

counter = 0
number = 1
while (number != 0):
	print()
	print(f"Try\x20\x23\x3a\x20\x5b{counter + 1}\x5d")
	print("Enter zero to exit.")

	try:
		number = int(input("Enter an integer: "))

		if number:
			numbers.add(number)
			counter += 1
		else:
			print("Leaving the program...")

	except Exception as e:
		number = 0
		print(e)

extracts = extract_of_evens_odds_primes(numbers)
summations = sum_of_evens_odds_primes(numbers)

print()
print("Sum of even, odd and prime numbers exercise.")
print(f"{numbers}")

first_header, second_header = 0, 1

print()
print("Extractions.")
print(f"Quantity: [{counter}].")

counter = 0
for row in extracts:
	print(f"{legends[first_header][counter]}.")
	print(f"+ Count : [{len(row)}].")
	print(f"+ Sum : [{sum(row)}].")
	counter += 1

	for stall in row:
		print(f"({stall})", end='\t')

	print("\n")

print("Summatories.")

counter = 0
for row in summations:
	print(f"{legends[first_header][counter]}.")
	counter += 1

	count = 0
	for stall in row:
		print(f"+ {legends[second_header][count]} : [{stall}].")
		count += 1

print()
print("Results.")
print(f"{extracts}")
print(f"{summations}")
