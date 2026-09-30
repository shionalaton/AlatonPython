alaton_flavor = input("Enter pizza flavor (Hawaiian/ Pepperoni/ Cheese): ").lower()

if alaton_flavor== "hawaiian":
    print("You selected Hawaiian Pizza.")

    alaton_size = input("Enter Size (Small/ Medium/ Large: ): ").lower()

    if alaton_size == "small":
       alaton_price = 250
    elif alaton_size == "medium":
       alaton_price = 350
    elif alaton_size== "large":
       alaton_price = 450
    else:
        alaton_price= 0
        print("Invalid Size.")



elif alaton_flavor== "cheese":
    print("You selected Whole Cheese Pizza.")

    alaton_size = input("Enter Size (Small/ Medium/ Large: ").lower()

    if alaton_size == "small":
        alaton_price = 250
    elif alaton_size == "medium":
        alaton_price = 350
    elif alaton_size == "large":
        alaton_price = 450
    else:
        alaton_price = 0
        print("Invalid Size.")



elif alaton_flavor== "pepperoni":
    print("You selected Pepperoni Pizza.")

    alaton_size = input("Enter Size (Small/ Medium/ Large: ").lower()

    if alaton_size == "small":
        alaton_price = 250
    elif alaton_size == "medium":
        alaton_price = 350
    elif alaton_size == "large":
        alaton_price = 450
    else:
        alaton_price = 0
        print("Invalid Size")

else:
    alaton_price = 0
    print("Invalid size.")
