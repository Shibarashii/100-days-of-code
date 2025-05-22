from calculator_art import logo


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Undefined"
    else:
        return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide

}


def calculator():
    calculating = True
    print(logo)
    num1 = int(input("What is the first number? "))

    for key in operations:
        print(key)

    while True:
        operation = input("Pick an operation ")
        if operation in ["+", '-', "*", "/"]:
            break

    num2 = int(input("What is the second number? "))

    calculation_function = operations[operation]
    result = calculation_function(num1, num2)

    print(f"{num1} {operation} {num2} = {result}")

    while True:
        continue_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a"
                                     f" new calculation ")
        if continue_calculating not in ["y", "n"]:
            continue

        if continue_calculating == "y":
            while True:
                operation = input("Pick an operation ")
                if operation in ["+", '-', "*", "/"]:
                    break

            prev_result = result
            num = int(input("What's the next number? "))
            calculation_function = operations[operation]
            result = calculation_function(result, num)
            print(f"{prev_result} {operation} {num} = {result} ")

        elif continue_calculating == "n":
            calculator()


calculator()
