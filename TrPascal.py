LIM_MIN = 0
LIM_MAX = 11

V_MINUS_ONE = -1
V_ONE = 1
V_ZERO = 0

def pascal_s_triangle(int_number_Rows : int):

	triangle_vector = []
	int_coeff_value = V_ZERO

	for int_n_row in range(int_number_Rows):
		current_row = []

		for int_n_col in range(int_n_row + V_ONE):
			if int_n_col == V_ZERO or int_n_col == int_n_row:
				int_coeff_value = V_ONE
			else:
				int_coeff_value = triangle_vector[int_n_row + V_MINUS_ONE][int_n_col + V_MINUS_ONE] + triangle_vector[int_n_row + V_MINUS_ONE][int_n_col]

			current_row.append(int_coeff_value)
			print(f"Row: [{int_n_row}]. Col: [{int_n_col}]. Value = [{int_coeff_value}].")

		print();
		triangle_vector.append(current_row)

	return triangle_vector


print("+---|----+---|----+---|----+---|----+---|----+---|----+")
print("|            Pascal's Triangle Generator.             |")
print("+---|----+---|----+---|----+---|----+---|----+---|----+")

int_n_Levels = int(input(f"Levels of Pascal's Triangle between [{LIM_MIN}] and [{LIM_MAX}] : "))

if int_n_Levels >= 0 and int_n_Levels <= 11:
	print(pascal_s_triangle(int_n_Levels))
else:
	print(f"¡Error! The value [{int_n_Levels}] is not between [{LIM_MIN}] and [{LIM_MAX}].")
