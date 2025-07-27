# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
CELSIUS_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius"""
    return (fahrenheit - CELSIUS_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit"""
    return (celsius / FAHRENHEIT_TO_CELSIUS_FACTOR) + CELSIUS_OFFSET

def main():
    print("Temperature Conversion Tool")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")

    try:
        choice = int(input("Enter your choice (1/2): "))
        temperature = float(input("Enter the temperature value: "))

        if choice == 1:
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted_temperature:.2f}°F")
        elif choice == 2:
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted_temperature:.2f}°C")
        else:
            print("Invalid choice. Please choose 1 or 2.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
