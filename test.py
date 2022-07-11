# 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)
# F = temp * 5/9 + 32
i = 5
cheel = 0
temp = float(input("What is the Temperature?: "))
fc = input("Farenheit or Celsius (F/C)?: ")
if fc == "C":
    temp = (temp * 5/9) + 32

while i < 64:
    cheel = 35.74 + 0.6215 * temp - 35.75 * (i ** 0.16) + 0.4275 * temp * (i ** 0.16)
    # print(f"At temperature {temp}F, and wind speed {i} mph, the windchill is: {"{:.2f}".format(cheel)}F")
    print(f"At temperature {temp}F, and wind speed {i} mph, the windchill is: {cheel}F")
    i += 5