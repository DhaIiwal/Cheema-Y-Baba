
while True:
    print("\nSimple Calculator")
    print("Enter 'q' to quit")

    num1 = input("First number: ")
    if num1.lower() == 'q':
        break

    op = input("Operator (+, -, *, /): ")
    num2 = input("Second number: ")

    try:
        num1 = float(num1)
        num2 = float(num2)

        if op == '+':
            print("Result:", num1 + num2)
        elif op == '-':
            print("Result:", num1 - num2)
        elif op == '*':
            print("Result:", num1 * num2)
        elif op == '/':
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                print("Result:", num1 / num2)
        else:
            print("Invalid operator")

    except:
        print("Invalid input, try again")