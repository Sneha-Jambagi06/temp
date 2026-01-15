import sys

# Check if command-line arguments are provided
if len(sys.argv) == 2:
    print("User provided input value")
    script_name = sys.argv[0]
    celsius = float(sys.argv[1])
else:
    print("No input given – using default value")
    script_name = sys.argv[0]
    celsius = 25.0   # default value

# Conversion formula
fahrenheit = (celsius * 9 / 5) + 32

# Display output
print("Script Name       :", script_name)
print("Celsius Temperature:", celsius)
print("Fahrenheit Result :", fahrenheit)
