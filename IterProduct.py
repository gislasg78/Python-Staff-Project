import itertools

vehicle_brands = ["Audi", "Bentley", "BMW", "Chevrolet", "Citroen",
                  "DS Automobiles", "Dacia", "Ford", "Fiat", "Hyundai",
                  "Honda", "Infiniti", "Kia", "Land Rover", "Lexus",
                  "Mazda", "Nissan", "Opel Z", "Peugeot", "Porsche",
                  "Renault", "Subaru", "Suzuki", "Tata", "Tesla",
                  "Toyota", "Volkswagen"]

vehicle_models = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]

def product_matrix(vehicle_brands, vehicle_models):
	motor_vehicles_at_dealership = None

	if isinstance(vehicle_brands, list):
		if isinstance(vehicle_models, list):
			motor_vehicles_at_dealership = itertools.product(vehicle_brands, vehicle_models)
		else:
			raise Exception("Vehicle models must be on some kind of list.")
	else:
		raise Exception("Vehicle brands must be on some kind of list.")

	return list(motor_vehicles_at_dealership)

print("Motor vehicles at dealership list.")

try:
	motor_vehicles_at_dealership_list = product_matrix(vehicle_brands, vehicle_models)

	print("+ List vehicles length: [{}].".format(len(motor_vehicles_at_dealership_list)))
	print("+ Vehicles content:")
	print(f"{motor_vehicles_at_dealership_list}")

except Exception as e:
	print(e)
