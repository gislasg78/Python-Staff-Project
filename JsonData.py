import json

my_string_dictionary = """
{
	"title": "Intermediate Python",
	"students":
	[
		{	"name": "Alice",
			"scores": [90, 85, 88, 78]
		},
		{
			"name": "Bob",
			"scores": [78, 82, 80, 89]
		},
		{
			"name": "Jane",
			"scores": [88, 74, 91, 73]
		},
		{
			"name": "Mark",
			"scores": [93, 66, 52, 33]
		},
		{
			"name": "Nick",
			"scores": [56, 73, 68, 84]
		}
	]
}
"""

def get_scores(my_str_dictionary):
	json_course_data = json.loads(my_str_dictionary)
	dict_sum_scores = {}

	for row_dict_key, row_dict_value in json_course_data.items():
		if row_dict_key == "students":
			for row_list_dict_item in row_dict_value:
				key_name = row_list_dict_item["name"]

				if not row_list_dict_item["name"] in dict_sum_scores:
					dict_sum_scores[row_list_dict_item["name"]] = 0

				if isinstance(row_list_dict_item["scores"], list):
					counter, summatory, average, minimum, maximum = 0, 0, 0, 0, 0

					if row_list_dict_item["scores"]:
						maximum = row_list_dict_item["scores"][0]
						minimum = row_list_dict_item["scores"][0]

						for item in row_list_dict_item["scores"]:
							counter += 1
							summatory += item

							if item > maximum:
								maximum = item

							if item < minimum:
								minimum = item

						average = summatory / counter

					dict_sum_scores[key_name] = [counter, summatory, average, minimum, maximum]

	return dict_sum_scores

dict_sum_scores = get_scores(my_string_dictionary)
print(f"{dict_sum_scores}")
