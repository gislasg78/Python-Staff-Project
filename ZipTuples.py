month_number_list = range(1, 13)

month_names_list = ["January", "February", "March", "April", "May", "June",
		"July", "August", "September", "October", "November", "December"]

month_days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

months_zip = zip(month_number_list, month_names_list, month_days_list)

months_iter = iter(month_names_list)
months_enum = enumerate(months_iter, start=1)

month_list = tuple(months_enum)
month_final_list = tuple(months_zip)

print("Tuple merged with an enumeration.")
print(f"{month_list}")

print("")
print("Merged tuples in tuples form.")
print(f"{month_final_list}")
