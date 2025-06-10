def index_all(search_list, item):
	indexes = list()

	for idx in range(len(search_list)):
		if search_list[idx] == item:
			indexes.append([idx])

		elif isinstance(search_list[idx], list):
			for subidx in index_all(search_list[idx], item):
				indexes.append([idx] + subidx)

	return indexes


print("Search for an item in a list.")
item = int(input("Enter the item to search for: "))

list_search = [[2, 2, 2], 3, 5, 5, [2, 2, 3], 3, 5, 5, [7, 7, 3], 3, 2, 2]
list_search = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
list_obtained = index_all(list_search, item)

print("")
print(f"Item searched:\t\t[{item}].")
print(f"Nested search list:\t{list_search}.")
print(f"Positions ​​obtained:\t{list_obtained}.")
