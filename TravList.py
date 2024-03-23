# Traversal of a list.

my_prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

print("List of prime numbers.")
for item in range(0, len(my_prime_list)):
    print(f"# [{item}]\t=\t[{my_prime_list[item]}].")

print()
print("Prime number sequence.")
for item in my_prime_list:
    print(f"[{item}].", end="\t")
