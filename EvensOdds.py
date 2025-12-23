def IsEven(number):
	return not(number % 2)

def IsOdd(number):
	return (number % 2)

def sum_of_evens_and_odds(numbers):
	addition_evens, counter_evens = 0, 0
	addition_odds, counter_odds = 0, 0

	for number in numbers:
		if (IsEven(number)):
			counter_evens += 1
			addition_evens += number

		if (IsOdd(number)):
			counter_odds += 1
			addition_odds += number

	return [[counter_evens, addition_evens], [counter_odds, addition_odds]]

def extract_of_evens_and_odds(numbers):
	return [sorted([x for x in numbers if IsEven(x)]),
		sorted([x for x in numbers if IsOdd(x)])]

legends = [["Evens", "Odds"], ["Count", "Sum"]]
numbers = [62, 66, 94, 97, 25, 11, 68, 54, 48, 67]
extract = extract_of_evens_and_odds(numbers)
result = sum_of_evens_and_odds(numbers)

print("Sum of even and odd numbers exercise.")
print("+ List:")
print(f"{numbers}")

print()
print("Summatories.")

counter = 0
for row in result:
	print(f"{legends[0][counter]}.")
	counter += 1

	count = 0
	for stall in row:
		print(f"+ {legends[1][count]} : [{stall}].")
		count += 1

print()
print("Extractions.")

counter = 0
for row in extract:
	print(f"{legends[0][counter]}.")
	print(f"+ Count : [{len(row)}].")
	print(f"+ Sum : [{sum(row)}].")
	counter += 1

	for stall in row:
		print(f"{stall}", end='\t')

	print("\n")

print()
print("Results.")
print(f"{result}")
print(f"{extract}")
