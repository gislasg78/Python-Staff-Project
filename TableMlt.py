# Program that generates lists containing lists of variable-sized lists of elements.

print("Highly dynamic pointer generator.")
n_matrix = int(input("How many rectangular arrangements do you want to create? : "))

matrix_matrix = []

print()
for m in range(0, n_matrix):
	print(f"For the matrix: [{m + 1}] of [{n_matrix}].")
	n_rows = int(input("How many lines will it generate for it? : "))

	matrix_rows = []
	for r in range(0, n_rows):
		print(f"For the matrix: [{m + 1}] of [{n_matrix}], and its row: [{r + 1}] of [{n_rows}].")
		n_cols = int(input("How many columns will it generate for it and its respective row? : "))

		matrix_cols = []
		for c in range(0, n_cols):
			value = int(input(f"Enter a value for Matrix: [{m + 1}] of [{n_matrix}] -> (Row: [{r + 1}] of [{n_rows}], Column: [{c + 1}] of [{n_cols}]) : "))
			matrix_cols.append(value)

		matrix_rows.append(matrix_cols)
		print()

	matrix_matrix.append(matrix_rows)
	print()

print()
print("Dump values of all dynamic pointers...")
print(matrix_matrix)

print()
n_matrix = 0
for m in matrix_matrix:
	n_matrix+=1
	print(f"Matrix: [{n_matrix}] of [{len(matrix_matrix)}].")

	n_rows=0
	for r in m:
		n_rows+=1
		print(f"\tRow: [{n_rows}] of [{len(m)}].")

		n_cols=0
		for c in r:
			n_cols+=1
			print(f"\t\tColumn: [{n_cols}] of [{len(r)}].", end='\t');
			print(f"Value: [{c}].")

		print()

	print()

print("End of the assigment!")
