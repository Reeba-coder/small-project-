def calculator(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
    else:
        return "Invalid operation"

# Usage
print(calculator("add", 10, 5))        # Output: 15
print(calculator("subtract", 20, 8))   # Output: 12
print(calculator("multiply", 4, 3))    # Output: 12
print(calculator("divide", 10, 2))     # Output: 5.0
print(calculator("divide", 10, 0))     # Output: Error: Cannot divide by zero
