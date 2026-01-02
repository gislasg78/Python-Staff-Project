import random

lower_limit = 1
upper_limit = 100

correct_number = random.randint(lower_limit, upper_limit)
factor = random.random()
guess = random.randrange(lower_limit, upper_limit)
guess_count = 0

list_of_guesses = list()
dict_of_guesses = {}
set_of_guesses = set()

print("Hi! Welcome to the guessing game.")
print(f"Please guess a number between: [{lower_limit}] and: [{upper_limit}].")
print(f"Chance factor of guessing: [{factor}].")
print(f"Suggested starting number: [{guess}].")
print("Type zero to give up!")
print()

while ((guess >= lower_limit) and (guess <= upper_limit)) and guess != correct_number and guess != 0:
	print(f"Tried\x20\x23: [{guess_count + 1}].")
	print("Enter zero to exit.")

	try:
		guess = int(input(f"What is your guest ({lower_limit} - {upper_limit})? : "))

		list_of_guesses.append(guess)

		if guess in dict_of_guesses:
			dict_of_guesses[guess] += 1
		else:
			dict_of_guesses[guess] = 1

		set_of_guesses.add(guess)

	except Exception as e:
		guess = 0
		print(e)

	if guess > correct_number:
		print(f"Wrong! You need to guess lower.\n")
	elif guess < correct_number:
		print(f"Wrong! You need to guess higher.\n")
	elif guess == correct_number:
		print("Well done. You guessed right!")
		print(f"[{guess}] = [{correct_number}].\n")

	guess_count += 1

print("Outcomes.")

if guess == correct_number:
	print("Congratulations!")
	print(f"The right answer was: [{correct_number}] with your last number: [{guess}].")
else:
	print("You failed!")
	print(f"Your last number: [{guess}] does not match the guessed number: [{correct_number}].")

print()
print("Numbers guessed:")
print(f"{list_of_guesses}")
print(f"{dict_of_guesses}")
print(f"{set_of_guesses}")

print()
print(f"It took you: [{guess_count}] guesses.")
