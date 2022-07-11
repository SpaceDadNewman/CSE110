import math
def compute_area_square(side):
    '''computes area of square'''
    area_square = side ** 2
    return area_square

def compute_area_rectangle(length, width):
    '''computes area of a rectangle'''
    area_rectangle = length * width
    return area_rectangle

def compute_area_circle(radius):
    '''computes area of a circle'''
    area_circle = math.pi * radius ** 2
    return area_circle

quit = 0 #ends the loop

while quit != 1:
    shape = input('What shape do you have? ')

    if shape == 'square':
        side = float(input('What is the length of the side of the square? '))
        area_square = compute_area_square(side)
        print(f'Square: {area_square}')

    if shape == 'rectangle' or 'square':
        length = float(input('What is the length of one side of the rectangle? '))
        width = float(input('What is the length of the other side of the rectangle? '))
        area_rectangle = compute_area_rectangle(length, width)
        print(f'Rectangle: {area_rectangle}')

    elif shape == 'circle':
        radius = float(input('What is the radius of the circle? '))
        area_circle = compute_area_circle(radius)
        print(f'Circle: {area_circle}')

    elif shape == 'quit':
        quit = 1

