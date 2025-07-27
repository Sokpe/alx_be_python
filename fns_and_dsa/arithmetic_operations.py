def perform_operation(num1, num2, operation):
    

    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y if y != 0 else "Error: Division by zero"
    }

    return operations.get(operation, lambda x, y: "Error: Invalid operation")(num1, num2)
