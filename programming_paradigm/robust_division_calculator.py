def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        return "Error: Both inputs must be numbers."

    try:
        result = numerator / denominator
        return f"{numerator} / {denominator} = {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

