# Fibonacci series from 'x' and 'y' up to 'n'.
LIM_MIN = 0
LIM_MAX = 45

dictFibo = {}
listFibo = []

# Recursive Fibonacci function.
def Fibo(n, x, y):
	if n<=1:
		return x+y
	else:
		return Fibo(n-1, y, x+y)

# Fibonacci function.
def fib(n, x, y):
	print()
	print("Generation of the Fibonacci series.")

	for i in range(0, n):
		print(f"#[{i}]\t:\t[{x}]\t+\t[{y}]\t=\t[{x+y}].")

		dictFibo[i] = [x, y, x+y]
		listFibo.append([x, y, x+y])

		x, y = y, x+y

	print()
	return y

# Main procedure.
print("+---|----+---|----+---|----+---|")
print("| Fibonacci's series Generator.|")
print("+---|----+---|----+---|----+---|")
n = int(input(f"Number of series from [{LIM_MIN}] to [{LIM_MAX}]: "))

if n>=LIM_MIN and n<=LIM_MAX:
	x = int(input("First number  : "))
	y = int(input("Second number : "))
	fib = fib(n, x, y)

	print()
	print(f"Latest Fibonacci result for [{x}] and [{y}] is: [{fib}] with [{n}] iterations.")

	print()
	print(f"Recursive Fibo of [{x}] and [{y}] is: [{Fibo(n,x,y)}] with [{n}] iterations.")

	print()
	print("List containing lists of the Fibonacci series.")
	print(listFibo)

	print()
	print("Dictionary containing lists of the Fibonacci series.")
	print(dictFibo)

	print()
	print("Dictionary breakdown of the Fibonacci series.")
	for key in dictFibo:
		print(f"#[{key}] :", end='\t')

		for value in dictFibo[key]:
			print(f"[{value}].", end='\t')

		print()

	print()
	print("Dictionary dump of the Fibonacci series.")
	for key, row in dictFibo.items():
		print(f"#[{key}] :", end='\t')

		for value in row:
			print(f"[{value}].", end='\t')

		print()

else:
	print(f"Error! The value: [{n}] is not between [{LIM_MIN}] and [{LIM_MAX}].")
