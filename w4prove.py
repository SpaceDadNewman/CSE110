# What is the price of a child's meal? 2.25
# What is the price of an adult's meal? 6.99
# How many children are there? 2
# How many adults are there? 1
# What is the sales tax rate? 4

# Subtotal: $11.49
# Sales Tax: $0.46
# Total: $11.95

# What is the payment amount? 20
# Change: $8.05

child_cost = float(input('What is the price of a child\'s meal? '))
adult_cost = float(input('What is the price of an adult\'s meal? '))
num_child = int(input('How many children are there? '))
num_adult = int(input('How many adults are there? '))
tax_rate = float(input('What is the sales tax rate? '))
print('\n')

subtotal = (child_cost * num_child + adult_cost * num_adult)

print(f'Subtotal: ${subtotal:.2f}')
print(f'Sales tax: ${subtotal * tax_rate / 100:.2f}')
tax = (subtotal * tax_rate / 100)
total = (subtotal + tax)
print(f'Total: ${total:.2f}')
print('\n')

coupon = input('Would you like to add a coupon? (y/n) ')
if coupon == 'y':
    percent = input('Which would you like to add to your purchase? \n\
        10% off     20% off     30% off (please input just the number): ')
    if percent == '10':
        total = (subtotal *.9 + tax)
    elif percent == '20':
        total = (subtotal *.8 + tax)
    elif percent == '30':
        total = (subtotal *.7 + tax)
    print(f'Your total is now ${total:.2f}')
    
payment = float(input('What is the payment amount? $'))
print(f'Change: ${payment - total:.2f}')
print('\n')