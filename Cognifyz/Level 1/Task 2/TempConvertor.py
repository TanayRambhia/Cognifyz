def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


print("Temperature Converter")
print("---------------------")
    
while True:
    try:
        temperature = float(input("Enter temperature value: "))
        unit = input("Enter unit of measurement (Celsius or Fahrenheit): ").lower()
        
        if unit == "celsius":
            converted_temperature = celsius_to_fahrenheit(temperature)
            target_unit = "Fahrenheit"
        elif unit == "fahrenheit":
            converted_temperature = fahrenheit_to_celsius(temperature)
            target_unit = "Celsius"
        else:
            print("Invalid unit of measurement. Please enter 'Celsius' or 'Fahrenheit'.")
            continue
            
        print(f"Converted temperature: {converted_temperature:.2f} {target_unit}")
        
        another_conversion = input("Do you want to perform another conversion? (yes/no): ").lower()
        if another_conversion != "yes":
            print("Exiting the program.")
            break
            
    except ValueError:
        print("Invalid input. Please enter a valid temperature value.")
