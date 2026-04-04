from add import add
from sub import subtract
from mul import multiply
from div import divide


def calculator():
    while True:
        print("\n===== Calculator =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please select between 1-5.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == '1':
            print("Result:", add(num1, num2))

        elif choice == '2':
            print("Result:", subtract(num1, num2))

        elif choice == '3':
            print("Result:", multiply(num1, num2))

        elif choice == '4':
            print("Result:", divide(num1, num2))


if __name__ == "__main__":
    calculator()
