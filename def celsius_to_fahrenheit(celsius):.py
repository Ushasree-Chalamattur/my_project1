def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter your choice (1 or 2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        return

    try:
        value = float(input("Enter the temperature value: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    if choice == '1':
        result = celsius_to_fahrenheit(value)
        print(f"{value} Celsius is equal to {result} Fahrenheit.")
    else:
        result = fahrenheit_to_celsius(value)
        print(f"{value} Fahrenheit is equal to {result} Celsius.")

temperature_converter()