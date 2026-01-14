import pickle

# Let's suppose we have a dictionary
my_dictionary = {"name": "John", "age": 30, "city": "Madrid", "country": "Spain"}

print("Data manipulation with Pickle.")

# We open a file in binary write mode
with open("datos.pkl", "wb") as my_file:  # "wb" = write binary
	pickle.dump(my_dictionary, my_file)

print()
print("Item saved with 'pickle'.")

# We open the file in binary read mode
with open("datos.pkl", "rb") as my_file:  # "rb" = read binary
    data_loaded = pickle.load(my_file)

print()
print("Object loaded with de-pickle:")

print()
print("File contents.")
print(data_loaded)
