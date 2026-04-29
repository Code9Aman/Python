#Temperature Converter - Convert between Celsius, Fahrenheit, and Kelvin with input validation and exception handling
def c_to_f(c):
    return (c*9/5) + 32
def c_to_k(c):
    return c + 273.15
def f_to_c(f):
    return (f-32)*5/9
def f_to_k(f):
    return (f-32)*5/9 + 273.15
def k_to_c(k):
    return k-273.15
def k_to_f(k):
    return (k-273.15)*9/5 + 32

temp = float(input("Enter temperature value: "))
from_unit = input("Enter unit (C/F/K): ").strip().upper()
to_unit = input("Convert to (C/F/K): ").strip().upper()



if from_unit == to_unit:
    result = temp
elif from_unit == "C" and to_unit == "F":
    result = c_to_f(temp)
elif from_unit == "C" and to_unit == "K":
    result = c_to_k(temp)
elif from_unit == "F" and to_unit == "C":
    result = f_to_c(temp)
elif from_unit == "F" and to_unit == "K":
    result = f_to_k(temp)
elif from_unit == "K" and to_unit == "C":
    result = k_to_c(temp)
elif from_unit == "K" and to_unit == "F":
    result = k_to_f(temp)
else:
    print("Invalid conversion.")
    result = None


if result is not None:
    if to_unit == "C":
        print(f"Result: {result:.2f} °C")
    elif to_unit == "F":
        print(f"Result: {result:.2f} °F")
    else:
        print(f"Result: {result:.2f} K")