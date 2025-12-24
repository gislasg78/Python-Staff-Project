# Program that obtains the remainder of an integer division.
# Test Values: 1. Dividen: 3650000. 2. Divisor: 2048.

def list_of_residuals(dividen : int, divisor : int):
	quotient = 0
	remainder = dividen
	list_remnant = []

	while (remainder >= divisor):
		list_remnant.append(remainder)
		remainder -= divisor

	list_remnant.append(remainder)

	return list_remnant

def remainder(dividen : int, divisor : int) -> int:
	return dividen - (divisor * (dividen // divisor))


print("Obtaining the remainder of an integer division.")
dividen = int(input("Dividen : "))
divisor = int(input("Divisor : "))

quotient = dividen // divisor
list_residues = list_of_residuals(dividen, divisor)
residual = remainder(dividen, divisor)

counter = 0
print()
print("List of residues.")

for item in list_residues:
	print(f"#[{counter}]\t:\t[{item}].")
	counter += 1

print(f"[{counter}] Obtained output results.")

print()
print("Division Results.")
print(f"+ Dividen:\t[{dividen}].")
print(f"+ Divisor:\t[{divisor}].")
print(f"+ Quotient:\t[{quotient}].")
print(f"+ Remainder:\t[{residual}].")

print()
print(f"The remainder of [{dividen}] divided by [{divisor}] is equal to [{residual}] with [{counter}] iterations.")
