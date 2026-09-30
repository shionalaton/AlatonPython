grade = int(input("Enter grade: "))
match grade:
    case n if 90 <= n <=100:
        print("Excellent")
    case n if 80 <= n <= 89:
        print("Very good")
    case n if 75 <= n <= 79:
        print("Passed")
    case n if 0 <= n <= 74:
        print("Failed")
    case _:
        print("Invalid grade")