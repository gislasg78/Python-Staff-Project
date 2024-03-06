# Lists, Tuples & Conjoins.

my_tuple = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
my_list = list(my_tuple)
my_conjoin = set(my_list)

print(f"The length of my tuple is: [{len(my_tuple)}].")
print(f"The content of my tuple is:\n{my_tuple}.")
print()
print(f"The length of my list is: [{len(my_list)}].")
print(f"The content of my list is:\n{my_list}.")
print()
print(f"The length of my conjoin is: [{len(my_conjoin)}].")
print(f"The content of my conjoin is:\n{my_conjoin}.")

print()
num = int(input("Number to search: "))

print()
print(f"The number: [{num}] is {num in my_tuple}.")
print(f"The number: [{num}] is in index: {my_tuple.index(num)}.")

print()
print(f"The number: [{num}] is {num in my_list}.")
print(f"The number: [{num}] is in index: {my_list.index(num)}.")

print()
print(f"The number: [{num}] is {num in my_conjoin}.")