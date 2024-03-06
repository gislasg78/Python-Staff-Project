# Generation of Pascal's Triangle.

LIM_MIN = 0
LIM_MAX = 11

V_MINUS_ONE = -1
V_ONE = 1
V_ZERO = 0


# Generating function of Pascal's Triangle.

def pascal_s_triangle(int_number_Rows : int):

	triangle_vector = []
	int_coeff_value = V_ZERO

	print()
	print("Breakdown of Pascal's Triangle values.")

	for int_n_row in range(int_number_Rows):
		current_row = []

		for int_n_col in range(int_n_row + V_ONE):
			if int_n_col == V_ZERO or int_n_col == int_n_row:
				int_coeff_value = V_ONE
			else:
				int_coeff_value = triangle_vector[int_n_row + V_MINUS_ONE][int_n_col + V_MINUS_ONE] + triangle_vector[int_n_row + V_MINUS_ONE][int_n_col]

			current_row.append(int_coeff_value)
			print(f"Row: [{int_n_row}].\tCol: [{int_n_col}].\tValue = [{int_coeff_value}].")

		print()
		triangle_vector.append(current_row)

	return triangle_vector


# Main procedure.

print("+---|----+---|----+---|----+---|")
print("| Pascal's Triangle Generator. |")
print("+---|----+---|----+---|----+---|")

int_n_Levels = int(input(f"Levels between [{LIM_MIN}] & [{LIM_MAX}] : "))

if int_n_Levels >= LIM_MIN and int_n_Levels <= LIM_MAX:
	psT = pascal_s_triangle(int_n_Levels)

	print("Pascal's Triangle Rows.")
	for row in psT:
		print(row)

	print()
	print("Element by element Dump.")
	for row in psT:
		for item in row:
			print(f"[{item}].", end="\t")

		print()

	print()
	print("Pascal's Triangle List.")
	print(psT)

else:
	print(f"¡Error! The value [{int_n_Levels}] is not between [{LIM_MIN}] and [{LIM_MAX}].")
