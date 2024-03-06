# Generation of Pascal's Triangle.
LIM_MIN = 0
LIM_MAX = 19

V_MINUS_ONE = -1
V_ONE = 1
V_ZERO = 0


# Generating function of Pascal's Triangle.
def pascal_s_triangle(rows : int):
	t_vector = []
	coeff_v = V_ZERO

	print()
	print("Breakdown of Pascal's Triangle values.")

	for row in range(rows):
		c_row = []

		for col in range(row + V_ONE):
			if col == V_ZERO or col == row:
				coeff_v = V_ONE
			else:
				coeff_v = t_vector[row + V_MINUS_ONE][col + V_MINUS_ONE] + t_vector[row + V_MINUS_ONE][col]

			c_row.append(coeff_v)
			print(f"Row: [{row}].\tCol: [{col}].\tValue = [{coeff_v}].")

		print()
		t_vector.append(c_row)

	return t_vector


# Main procedure.
print("+---|----+---|----+---|----+---|")
print("| Pascal's Triangle Generator. |")
print("+---|----+---|----+---|----+---|")

levels = int(input(f"Levels between [{LIM_MIN}] & [{LIM_MAX}] : "))

if levels >= LIM_MIN and levels <= LIM_MAX:
	psT = pascal_s_triangle(levels)

	print("Pascal's Triangle Rows.")
	for row in psT:
		print(row)

	print()
	print("Element by Element Dump.")
	for row in psT:
		for item in row:
			print(f"[{item}].", end="\t")

		print()

	print()
	print("Pascal's Triangle List.")
	print(psT)

else:
	print(f"Error! The value [{levels}] is not between [{LIM_MIN}] and [{LIM_MAX}].")
