#Temperature Converter - Convert between Celsius, Fahrenheit, and Kelvin with input validation and exception handling


#C= 5/9(F-32)
#K=5/9(F-32)+ 273.15


#logic for coversion
def celsius_to_kelvin(c):
    return  c + 273.15
def celsius_to_farenh(c):
    return  (c*9/5) + 32
def kelvin_to_celsius(k):
    return k - 273.15
def kelvin_to_farenh(k):
    return (9/5*(k-273.15)) + 32
def farenh_to_celsius(f):
    return 5/9*(f-32)
def farenh_to_kelvin(f):
    return (5/9*(f-32) + 273.15)

temp_value = float(input("Enter the temperature value :"))
from_scale = input("Enter the temperature scale(C/K/F) :").lower()
to_scale = input("Enter the scale to be converted into(C/K/F) :").lower()

if from_scale==to_scale:
    result = temp_value
elif from_scale=="c" and to_scale=="k":
    result=celsius_to_farenh(temp_value)
elif from_scale=="c" and to_scale=="f":
    result = celsius_to_kelvin(temp_value)
elif from_scale=="k" and to_scale=="f":
    result = kelvin_to_farenh(temp_value)
elif from_scale=="k" and to_scale=="c":
    result = kelvin_to_celsius(temp_value)
elif from_scale=="f" and to_scale=="k":
    result = farenh_to_kelvin(temp_value)
elif from_scale=="f" and to_scale=="c":
    result = farenh_to_celsius(temp_value)
else:
    print("Invalid Prompt")
    result = None

if result is not None:
    if to_scale == "c":
        print(f"Result: {result:.2f} °c")
    elif to_scale == "f":
        print(f"Result: {result:.2f} °f")
    else:
        print(f"Result: {result:.2f} k")


