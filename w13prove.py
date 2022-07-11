#  Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)
#  F = (C * 9/5) + 32

def calc_celsius(temp):
    temp = (float(temp) * 9/5) + 32
    return temp

def calc_chill(temp, speed):
    chill = 35.74 + (.6215 * temp) - 35.75 * (speed ** .16) + .4275 * temp * (speed ** .16)
    return chill

temp = input('What is the temperature?: ')
speed = 5
version = input('Fahrenheit or Celsius (F/C)?: ')
if version == 'F':
    temp = float(temp)
elif version == 'C':
    temp = calc_celsius(temp)

while speed <= 60:
    chill = calc_chill(temp, speed)
    print(f'At temperature {temp}{version}, and wind speed {speed} mph, the windchill is: {"{:.2f}".format(chill)}F')
    speed += 5