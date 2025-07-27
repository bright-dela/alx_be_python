FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celcius):
    return (celcius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def temperature_converter():

    while True:
        temperature_input = input("Enter the temperature to convert: ")

        if temperature_input.isdigit():
            temperature = float(temperature_input)
            break
        else:
            print("Invalid temperature. Please enter a numeric value.")

    while True:
        temp_type = input(
            "Is this temperature in Celsius or Fahrenheit? (C/F): "
        ).upper()

        if temp_type in ("C", "F"):
            break
        else:
            print("Invalid input.")

    if temp_type == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result:.2f}°C")

    elif temp_type == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result:.2f}°F")


if __name__ == "__main__":
    temperature_converter()
