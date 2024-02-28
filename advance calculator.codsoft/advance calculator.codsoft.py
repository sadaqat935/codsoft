import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(x) 

def cube(x):
    return x ** 3

def square(x):
    return x ** 2

def calculator():
    print("Welcome to the Advanced Calculator!")
    history = []

    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Square Root")
        print("7. Cube")
        print("8. Square")
        print("9. Show History")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == '10':
            print("Goodbye!")
            break
        elif choice == '9':
            if not history:
                print("No calculations in history.")
            else:
                print("\nCalculation History:")
                for i, calculation in enumerate(history, start=1):
                    print(f"{i}. {calculation}")
            break

        try:
            num1 = float(input("Enter the first number: "))
            if choice not in ['6', '7', '8']:
                num2 = float(input("Enter the second number: "))

            result = None
            operation_str = None
            if choice == '1':
                result = add(num1, num2)
                operation_str = f"{num1} + {num2}"
            elif choice == '2':
                result = subtract(num1, num2)
                operation_str = f"{num1} - {num2}"
            elif choice == '3':
                result = multiply(num1, num2)
                operation_str = f"{num1} * {num2}"
            elif choice == '4':
                result = divide(num1, num2)
                operation_str = f"{num1} / {num2}"
            elif choice == '5':
                result = power(num1, num2)
                operation_str = f"{num1} ^ {num2}"
            elif choice == '6':
                result = square_root(num1)
                operation_str = f"sqrt({num1})"
            elif choice == '7':
                result = cube(num1)
                operation_str = f"{num1} ^ 3"
            elif choice == '8':
                result = square(num1)
                operation_str = f"{num1} ^ 2"

            if result is not None:
                print(f"The result is: {result}")
                history.append(f"{operation_str} = {result}")

            more_operations = input("Do you want to perform more operations? (yes/no): ").lower()
            if more_operations != 'yes':
                print("Goodbye!")
                break

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculator()
