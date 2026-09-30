
print("============= NU CURRICULUM =============")

print("96% - 100%  4.0         ")
print("90% - 95%   3.5         ")
print("84% - 89%   3.0         ")
print("78% - 83%   2.5         ")
print("72% - 72%   2.0         ")
print("66% - 71%   1.5         ")
print("60% - 65%   1.0         ")


Alaton_grade = float(input("Enter Grade:     "))


match Alaton_grade:
    case 4.0:
        print("96 - 100")

    case 3.5:
        print("90 - 100")

    case 3.0:
        print("84 - 90")

    case 2.5:
        print("78- 83")

    case 2.0:
        print("72-72")

    case 1.5:
        print("66-71")

    case 1.0:
        print("60-65")


    case _:
        print("Not in range")








