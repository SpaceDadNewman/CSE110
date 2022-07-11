import math

i = 1 
user_choice = int(input('How many columns and rows do you want in your multiplication table? '))

max_number = user_choice * user_choice
num_digits = int(math.log10(max_number)) + 1
range_max = user_choice + 1

for numbers in range(1,range_max):
    for number in range(1,range_max):
        value = numbers * number
        print(f'{value:{num_digits}}', end=' ')
    print('\n')
    i+=1

    #{hair.title():<16} Eyes: {eyes.title()}