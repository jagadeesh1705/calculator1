def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


if __name__ == "__main__":
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", divide(num1, num2))
    except ValueError:
        print("Invalid input")
