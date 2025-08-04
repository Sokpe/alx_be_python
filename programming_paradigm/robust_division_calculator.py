def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = numerator / denominator
        return f"{numerator} / {denominator} = {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."


