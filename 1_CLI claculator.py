# Project 01: CLI Calculator
# Supports: +, -, *, /, %

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Modulus by zero is not allowed.")
    return a % b


def calculate(a, operator, b):
    """Dispatch calculation based on operator."""
    if operator == '+':
        return add(a, b)
    elif operator == '-':
        return subtract(a, b)
    elif operator == '*':
        return multiply(a, b)
    elif operator == '/':
        return divide(a, b)
    elif operator == '%':
        return modulus(a, b)
    else:
        raise ValueError("Invalid operator.")


def display_result(result):
    """Display the calculation result."""
    print(f"Result: {result}")


def ask_continue():
    """Ask user whether to continue."""
    while True:
        choice = input("Do you want to continue? (y/n): ").strip().lower()
        if choice in ['y', 'n']:
            return choice
        print("Please enter 'y' or 'n'.")


def main():
    print("=== CLI Calculator ===")

    while True:
        try:
            first_number = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /, %): ").strip()
            second_number = float(input("Enter second number: "))

            result = calculate(first_number, operator, second_number)
            display_result(result)

        except ValueError as e:
            print(f"Input Error: {e}")
        except ZeroDivisionError as e:
            print(f"Math Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

        if ask_continue() == 'n':
            print("Exiting calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()
