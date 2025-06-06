def calculate_average(item_tuple):
	assert len(item_tuple), "The tuple does not contain any elements, therefore it is empty."
	return sum(item_tuple) / len(item_tuple)


item_tuple = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)

try:
	average = calculate_average(item_tuple)

	print(f"The elements contained in the tuple are:")
	print(f"{item_tuple}.")
	print(f"Its average is: [{average}].")
except Exception as e:
	print(f"This function threw the following exception:")
	print(f"[{e}].")
