

print("============Student Grade===============")

print("97% - 100% Dark Green       ")
print("90% - 96%  Light Green      ")
print("80% - 89%  Yellow Green     ")
print("70% - 79%  Yellow           ")


Alaton_name = input("Enter Student Name:      ")
Alaton_score = int(input("Enter Student Score:    "))
Alaton_total = int(input("Total Items: "))

Alaton_percentage = (Alaton_score / Alaton_total)*100
Alaton_passing = (Alaton_total*.60)

if Alaton_percentage >= 97 and Alaton_percentage <= 100:
    Alaton_color = "Dark Green"
    Alaton_result = "Passed"

elif Alaton_percentage >= 90 and Alaton_percentage <= 96:
    Alaton_color = "Light Green"
    Alaton_result = "Passed"

elif Alaton_percentage >= 80 and Alaton_percentage <= 89:
    Alaton_color = "Yellow Green"
    Alaton_Alaton_result = "Passed"

elif Alaton_percentage >= 70 and Alaton_percentage <= 79:
    Alaton_color = "Yellow"
    Alaton_colorresult = "Passed"

elif Alaton_percentage >= 60 and Alaton_percentage <= 69:
    Alaton_color = "Orange"
    ALaton_result = "Passed"

else:
    Alaton_color = "Red"
    Alaton_result = "Failed"

print(f"Passing Score: {Alaton_passing}")
print(f"Score Percentage: {Alaton_percentage:.2f}")
print(f"Color: {Alaton_color}")
print(f"Result: {Alaton_result}")

