from math import pi, pow
Radius = int(input("Enter radius: "))
try:
    if Radius < 0:
        raise ValueError
    area = pi * pow(Radius,2)
except ValueError:
    print("Enter radius greater than 0.")
else:
    print(f'The area of circle is: {area}.')
finally:
    print("This is calculated area of circle.")