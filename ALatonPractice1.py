#practice 1
students = {
    "Ana": 85,
    "Ben": 90,
    "Carlo": 78,
    "Diana": 96
}
print("STUDENTS GRADES")
print("------------------")
print("Ana", students["Ana"])
print("Ben", students["Ben"])

students["Deanleo"] = 88
#update student's grade
students["Bobet"] = 82
students["Siahmarie"] = 91
name1 = input("Enter students name: ")
grade1 = int(input("Enter grade: "))
students[name1] = grade1
print(students)
print("\nUpdated Student Grades")
print("------------------------")
for name, grade in students.items():
    print(name, ":", grade)
#search a student
search = input("\nEnter student name to search: ")
if search in students:
    print(search, "has a grade of", students[search])
else:
    print("Student not found.")
lowest = min(students.values())
print("Lowest grade: ", lowest)
highest = max(students.values())
print("Highest grade: ", highest)
diff = highest - lowest
print("difference: ", diff)
average = diff / len(students)
print("Average grade: ", average)
sort = sorted(students)
print("Sorted:", sort)

