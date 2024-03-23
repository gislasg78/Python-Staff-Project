# Lists & Conjoins.

my_prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
my_even_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
my_odd_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]

my_prime_set = set(my_prime_list)
my_even_set = set(my_even_list)
my_odd_set = set(my_odd_list)

print(f"Prime Numbers Set:\n{my_prime_set}.")

union = my_even_set | my_odd_set
print()
print(f"Union Pairs & Odds as a new set:\n{union}.")

onlyeven = my_even_set - my_prime_set
print()
print(f"Only Evens not in Prime Numbers:\n{onlyeven}.")

onlyodds = my_odd_set - my_prime_set
print()
print(f"Only Odds not in Prime Numbers:\n{onlyodds}.")

intersectionodds = my_odd_set & my_prime_set
print()
print(f"Intersection of Odds in Prime Numbers:\n{intersectionodds}.")

intersectionevens = my_even_set & my_prime_set
print()
print(f"Intersection of Evens in Prime Numbers:\n{intersectionevens}.")
