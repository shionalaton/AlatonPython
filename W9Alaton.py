
Alaton_name = str(input("Enter your name: ")).title()
print(f"\nHi, {Alaton_name}\n")

choice = input("Your Choices of Calculation:\n 1.power 2. voltage 3. current:\n")

if choice == "1":

    Alaton_Voltage = float(input("Voltage: "))
    Alaton_Current = float(input("Current: "))
    Alaton_result = Alaton_Current * Alaton_Voltage
    print("Your Power: {Alaton_result: .2f}")

elif choice == "2":

    Alaton_Current = float(input("Current: "))
    Alaton_Power = float(input("Power: "))
    Alaton_result = Alaton_Power / Alaton_Current
    print(f"Your Voltage: {Alaton_result: .2f}")

if choice == "3":

    Alaton_Voltage = float(input("Voltage: "))
    Alaton_Power = float(input("Power: "))
    Alaton_result = Alaton_Power / Alaton_Voltage
    print(f"Your Current: {Alaton_result: .2f}")

