# Inheritance in Python.
class Figure:
	def __init__(self, name):
		self.name = name

	def get_name(self):
		return self.name

	def area(self):
		pass

	def perimeter(self):
		pass

class Triangle(Figure):
	def __init__(self, name):
		super().__init__(name)

	def area(self, base, height):
		self.base = base
		self.height = height
		return (self.base * self.height) / 2

	def perimeter(self, side):
		self.side = side
		return 3 * self.side


class Square(Figure):
	def __init__(self, name):
		super().__init__(name)

	def area(self, side):
		self.side = side
		return self.side ** 2

	def perimeter(self, side):
		self.side = side
		return 4 * self.side


class Rectangle(Figure):
	def __init__(self, name):
		super().__init__(name)

	def area(self, base, height):
		self.base = base
		self.height = height
		return self.base * self.height

	def perimeter(self, base, height):
		self.base = base
		self.height = height
		return 2 * self.base + 2 * self.height


class Circle(Figure):
	def __init__(self, name):
		super().__init__(name)
		self.PI = 3.1416

	def area(self, radius):
		self.radius = radius
		return self.PI * self.radius ** 2

	def perimeter(self, radius):
		self.radius = radius
		return 2 * self.radius * self.PI


class Diamond(Figure):
	def __init__(self, name):
		super().__init__(name)

	def area(self, larger_d, smaller_d):
		self.larger_d = larger_d
		self.smaller_d = smaller_d
		return (self.larger_d * self.smaller_d) / 2

	def perimeter(self, side):
		self.side = side
		return 4 * self.side

# Main procedure.
triangle = Triangle("Triangle")
square = Square("Square")
rectangle = Rectangle("Rectangle")
circle = Circle("Circle")
diamond = Diamond("Diamond")

print("Basic geometric figures.")
print("Calculation of areas and perimeters.")
print()

t_base = float(input("Triangle base: "))
t_height = float(input("Triangle height: "))
t_area = triangle.area(t_base, t_height)
t_perimeter = triangle.perimeter(t_base)

print()
s_side = float(input("Side of the square: "))
s_area = square.area(s_side)
s_perimeter = square.perimeter(s_side)

print()
r_base = float(input("Rectangle base: "))
r_height = float(input("Rectangle height: "))
r_area = rectangle.area(r_base, r_height)
r_perimeter = rectangle.perimeter(r_base, r_height)

print()
c_radius = float(input("Circle radius: "))
c_area = circle.area(c_radius)
c_perimeter = circle.perimeter(c_radius)

print()
d_larger_d = float(input("Diamond larger diameter: "))
d_smaller_d = float(input("Diamond smaller diameter: "))
d_area = diamond.area(d_larger_d, d_smaller_d)
d_perimeter = diamond.perimeter(d_larger_d)

print()
print("Results.")
print("Figure:\t[", triangle.get_name(), "].\tArea:\t[", t_area, "].\tPerimeter:\t[", t_perimeter, "].")
print("Figure:\t[", square.get_name(), "].\tArea:\t[", s_area, "].\tPerimeter:\t[", s_perimeter, "].")
print("Figure:\t[", rectangle.get_name(), "].\tArea:\t[", r_area, "].\tPerimeter:\t[", r_perimeter, "].")
print("Figure:\t[", circle.get_name(), "].\tArea:\t[", c_area, "].\tPerimeter:\t[", c_perimeter, "].")
print("Figure:\t[", diamond.get_name(), "].\tArea:\t[", d_area, "].\tPerimeter:\t[", d_perimeter, "].")
