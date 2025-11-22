# Random Module.
import random
from datetime import datetime

# Random Ticket Function.
def ticket(nums_by_ticket, minimum, maximum):
	return list(sorted(random.sample(range(minimum, maximum), nums_by_ticket)))

# Random Tickets Generator.
def tickets(quantity_tickets, nums_by_ticket, minimum, maximum):
	myTickets = []

	for i in range(0, quantity_tickets):
		print(f"\nTicket: [{i + 1}] of: [{quantity_tickets}].")

		for j in range(0, nums_by_ticket):
			lotteryWinners = ticket(nums_by_ticket, minimum, maximum)
			print(f"#: {j + 1} = {lotteryWinners}.")
			myTickets.append(lotteryWinners)

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
print("Random number generation for Melate.")
quantity_tickets = int(input("Number of tickets: "))

print()
print("List of randomly generated tickets.")
print(datetime.now().strftime("[%A, %B %d, %Y] - [%H:%M:%S]."))

list_of_tickets = tickets(quantity_tickets, 6, 1, 48)

cards = ["Jack", "Queen", "King", "Ace"]
print()
print(f"Card: [{random.choice(cards)}].")
