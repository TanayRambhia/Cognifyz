def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def modulo(x, y):
    if y == 0:
        raise ValueError("Cannot perform modulo operation with zero.")
    return x % y

def main():
    print("Basic Calculator")
    print("----------------")

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /, %): ")
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        elif operator == "%":
            result = modulo(num1, num2)
        else:
            print("Invalid operator.")
            return

        print(f"Result: {result:.2f}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

if __name__ == "__main__":
    main()
