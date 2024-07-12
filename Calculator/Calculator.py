while True:
    print("Select an Operation to perform: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    operation = input("Please choose your operation: ")

    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    if operation == "1":
        print("The sum of the numbers after addition is: " + str(int(num1) + int(num2)))
    elif operation == "2":
        print("The result of the numbers after subtraction is: " + str(int(num1) - int(num2)))
    elif operation == "3":
        print("The result of the numbers after multiplication is: " + str(int(num1) * int(num2)))
    elif operation == "4":
        print("The result of the numbers after division is: " + str(int(num1) / int(num2)))
    else:
        print("Invalid Entry")
    
    print("Do you want to perform another operation?")
    print("1. Yes")
    print("2. No")

    continue_choice = input("Please choose 1 or 2: ")

    if continue_choice != "1":
        print("Exiting the program.")
        break

    print()  
