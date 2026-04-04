def add(a, b):
    return a + b


if __name__ == "__main__":
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", add(num1, num2))
    except ValueError:
        print("Invalid input")
