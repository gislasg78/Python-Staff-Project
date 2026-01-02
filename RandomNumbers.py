# Random Module.
import random
from datetime import datetime

# Random Ticket Function.
def ticket(nums_by_ticket, minimum, maximum):
	try:
		return list(sorted(random.sample(range(minimum, maximum), nums_by_ticket)))
	except Exception as e:
		print(e)
		return list()

# Random Tickets Generator.
def tickets(quantity_tickets, nums_by_ticket, minimum, maximum):
	myTickets = []

	for i in range(0, quantity_tickets):
		print(f"\nTicket\x20\x23\x3a [{i + 1}] of: [{quantity_tickets}]\x2e")

		for j in range(0, nums_by_ticket):
			try:
				lotteryWinners = ticket(nums_by_ticket, minimum, maximum)

				if lotteryWinners:
					print(f"\x23\x3a {j + 1} \x3d {lotteryWinners}\x2e")
					myTickets.append(lotteryWinners)

			except Exception as e:
				print(e)

	return myTickets

# Random Numbers.
print("Random Numbers Generator.")
print(f"{datetime.now()}")

print()
print(f"[{random.random()}].")
list_decider = ["HEADS", "TAILS"]
decider = random.randrange(len(list_decider))
print(f"[{list_decider[decider]}].")

print("You rolled a: [" + str(random.randrange(1, 7)) + "].")

# Random Choices.
print()
print("Random number generation for Lottery.")

try:
	quantity_tickets = int(input("Number of tickets: "))
	numbers_by_ticket = int(input("Numbers per ticket: "))
	minimum_value = int(input("Minimum value: "))
	maximum_value = int(input("Maximum value: "))
except Exception as e:
	print(e)
	quantity_tickets, numbers_by_tickets, minimum_value, maximum_value = 0, 0, 0, 0

print()
print("List of randomly generated tickets.")
print(datetime.now().strftime("[%A, %B %d, %Y] - [%H:%M:%S]."))

if quantity_tickets and numbers_by_ticket and minimum_value and maximum_value:
	print("Processing tickets...")
	list_of_tickets = tickets(quantity_tickets, numbers_by_ticket, minimum_value, maximum_value + 1)
else:
	print("Error! The requested tickets were not processed.")
	list_of_tickets = []

cards = ["Jack", "Queen", "King", "Ace"]
print()
print(f"Card: [{random.choice(cards)}].")
