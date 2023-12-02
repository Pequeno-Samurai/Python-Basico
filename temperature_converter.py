# Convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5.0 / 9.0)

# Convert Fahrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * (5.0 / 9.0) + 273.15

# Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * (9.0 / 5.0)) + 32

# Convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Convert Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * (9.0 / 5.0) + 32

# Main function
def main():
    # Options menu
    option = 0

    while option != 7:
        print("1. Convert Fahrenheit to Celsius")
        print("2. Convert Celsius to Fahrenheit")
        print("3. Convert Kelvin to Celsius")
        print("4. Convert Celsius to Kelvin")
        print("5. Convert Fahrenheit to Kelvin")
        print("6. Convert Kelvin to Fahrenheit")
        print("7. Exit")
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("\nInvalid input. Please enter a number.")
            continue

        if option == 1:
            print("Enter temperature in Fahrenheit: ")
            try:
                fahrenheit = float(input())
                print(f"\nTemperature in Celsius: {fahrenheit_to_celsius(fahrenheit)}")
            except ValueError:
                print("\nInvalid input. Please enter a number.")
        elif option == 2:
            print("Enter temperature in Celsius: ")
            try:
                celsius = float(input())
                print(f"\nTemperature in Fahrenheit: {celsius_to_fahrenheit(celsius)}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif option == 3:
            print("Enter temperature in Kelvin: ")
            try:
                kelvin = float(input())
                print(f"\nTemperature in Celsius: {kelvin_to_celsius(kelvin)}")
            except ValueError:
                print("\nInvalid input. Please enter a number.")
        elif option == 4:
            print("Enter temperature in Celsius: ")
            try:
                celsius = float(input())
                print(f"\nTemperature in Kelvin: {celsius_to_kelvin(celsius)}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif option == 5:
            print("Enter temperature in Fahrenheit: ")
            try:
                fahrenheit = float(input())
                print(f"\nTemperature in Kelvin: {fahrenheit_to_kelvin(fahrenheit)}")
            except ValueError:
                print("\nInvalid input. Please enter a number.")
        elif option == 6:
            print("Enter temperature in Kelvin: ")
            try:
                kelvin = float(input())
                print(f"\nTemperature in Fahrenheit: {kelvin_to_fahrenheit(kelvin)}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif option == 7:
            print("Goodbye!")
        else:
            print("Invalid option. Please enter a valid option.")

# Call main function
if __name__ == '__main__':
    main()
