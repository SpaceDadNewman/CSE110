import math
square = float (input('What is the length of one side of the square in centimeters? '))
print(f'The area of the square is: {square ** 2} centimeters and {square ** 2 / 100} meters')
rec_len = float (input('What is the length of rectangle in centimeters? '))
rec_wid = float (input ('What is the width of the rectangle in centimeters? '))
print(f'The area of the rectangle is: {rec_len * rec_wid} centimeters and {(rec_len * rec_wid) / 100} meters')
radius = float (input('What is the radius of the circle in centimeters? '))
print(f'The area of the circle is: {math.pi * radius ** 2} centimeters and {math.pi * radius ** 2 / 100}')

length = float(input('Input a single length: '))
print(f'The area of a square with that length is: {length ** 2}')
print(f'The area of a circle with that length is: {math.pi * length ** 2}')
print(f'The volume of a cube with that length is: {length ** 3}')
print(f'The volume of a sphere with that length is: {4/3 * math.pi * length ** 2}')
    
centi = float(input('Input a value in centimeters: '))
print(f'The area in centimeters is: {centi ** 2}')
print(f'The area in meters is: {centi ** 2 / 100}')