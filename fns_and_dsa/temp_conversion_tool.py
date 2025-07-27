# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    print("Temperature Conversion Tool")

    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

        if unit.upper() == 'C':
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted_temperature:.2f}°F")
        elif unit.upper() == 'F':
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted_temperature:.2f}°C")
        else:
            print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()