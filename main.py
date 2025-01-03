
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) +32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

temperature = float(input("Enter temperature value: "))
unit = input("Enter the unit (Celsius, Fahrenheit, or Kelvin): ").strip().lower()

if unit == "celsius":
    fahrenheit_temperature = celsius_to_fahrenheit(temperature)
    kelvin_temperature = celsius_to_kelvin(temperature)
    print(f"{temperature} degrees Celsius is equal to {fahrenheit_temperature} degrees Fahrenheit")
    print(f"{temperature} degrees Celsius is equal to {kelvin_temperature} degrees Kelvin")



