# Program that validates the largest of three integers.

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))

if num1>=num2 and num1>=num3:
    print(f"The first number: [{num1}] is greater than second number: [{num2}] and third number: [{num3}].")
elif num2>=num1 and num2>=num3:
    print(f"The second number: [{num2}] is greater than first number: [{num1}] and third number: [{num3}].")
elif num3>=num1 and num3>=num2:
    print(f"The third number: [{num3}] is greater than first number: [{num1}] and second number: [{num2}].")