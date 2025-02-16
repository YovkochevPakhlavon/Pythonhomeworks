def convert_far_to_cel():
    F = float(input("Enter a temperature in degrees Fahrenheit: "))
    C = (F - 32) * 5/9
    print(f'{F} degrees F = {round(C,2)} degrees C')

def convert_cel_to_far():
    cel = float(input("Enter a temperature in degrees Celsius: "))
    F = cel * 9/5 + 32
    print(f'{cel} degrees C = {round(F,2)} degrees F')

convert_far_to_cel()
convert_cel_to_far()