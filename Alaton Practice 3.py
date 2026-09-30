#practice 3
from Alatonpatient import highest

students = {}
number = int(input("Enter number of students: "))
for i in range(number):
    print("\nStudent", i + 1)
    name = input("Enter student name: ")
    grade1 = float(input("Enter Grade 1: "))
    grade2 = float(input("Enter Grade 2: "))
    grade3 = float(input("Enter Grade 3: "))
    students[name] = (grade1, grade2, grade3)
print("\n=============STUDENTS RECORDS=================")
highest = 0
namehighest = ""
tally = 0
for name, grades in students.items():
    average = sum(grades) / len(grades)
    print(name, *grades, "Average: ", round(average, 2))

    if average > highest:
        highest = average
        namehighest = name








