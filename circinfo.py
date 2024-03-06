# Area and perimeter of a circle.

PI = 3.1416

radius = float(input("Enter the circle radius value: "))

circle_perimeter = PI * 2 * radius
circle_area = PI * radius ** 2

print()
print("Circle Information.")
print(f"Perimeter:\t[{circle_perimeter:.4f}].")
print(f"Area:\t\t[{circle_area:.4f}].")
