import random

class Student:
	def __init__(self, name, score=0.00):
		self.name = name
		self.score = score

	def __repr__(self):
		return f"(name=[{self.name}], score=[{self.score:.2}])"

students = [Student("Joe", round(random.random(), 2)), Student("Amy", round(random.random(), 2)), Student("Mark", round(random.random(), 2)), Student("Zach", round(random.random(), 2)), Student("Jane", round(random.random(), 2)), Student("Sarah", round(random.random(), 2)), Student("Mary", round(random.random(), 2))]

print("Practice for manipulating maps, filters, and classes with lists.")

print()
print("List of available students with their scores.")
for item in students:
	print(item)

top_limit = round(random.random(), 2)

print()
print(f"Top limit: [{top_limit}].")

students_results = []

for student in students:
	students_results.append([student.name, student.score, "Passed"]) if student.score >= top_limit else students_results.append([student.name, student.score, "Failed"])

map_results = list(map(lambda student: [student.name, student.score, "Passed"] if student.score >= top_limit else [student.name, student.score, "Failed"], students))
filter_outcomes_ge = list(filter(lambda student: student.score >= top_limit, students))
filter_outcomes_lt = list(filter(lambda student: student.score < top_limit, students))

print()
print("List of Students with Qualifying Scores.")
print(students_results)

print()
print("Map of Students with Qualifying Scores.")
print(map_results)

print()
print("Filter of Students with Qualifying Scores.")
print(filter_outcomes_ge)
print()
print(filter_outcomes_lt)

from functools import reduce

reduce_total = reduce(lambda total, student: student.score + total, students, 0)

print()
print("Output results by reduction.")
print(f"Sum: [{reduce_total:.2}].")
print(f"Avg: [{reduce_total/len(students):.2}].")
