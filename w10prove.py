items = []
prices = []
quantity = []
total = float(0)
quit = 0
count = 1

#this while operates as the quit function
while quit != 1:

    choice2 = input('Please select one of the following: \n\
    1. Add Item \n\
    2. View Cart \n\
    3. Remove Cart \n\
    4. Compute Total \n\
    5. Quit \n')

    #asks user for item and price - WORKING
    item = None
    price = None
    amount = None
    if choice2 == '1':
        item = input('What item would you like to add? ')
        items.append(item)
        amount = int(input(f'How many of "{item}" would you like? '))
        quantity.append(amount)
        price = float(input(f'What is the price of \'{item}\' $'))
        price = price * amount
        prices.append(price)
        count += 1  #this is used for the remove function
        print(f'\'{item}\' has been added to the cart')

    #list care items - WORKING
    count = len(items)
    if choice2 == '2':
        print('The contents of your cart are:')
        for i in range(len(items)):
            item = items[i]
            print(f'{i + 1}. {quantity[i]}x {items[i]} - ${"{:.2f}".format(prices[i])}')

    #removes items - WORKING
    if choice2 == '3':
        remove = int(input('Which item would you like to remove? '))
        remove -= 1
        del items[remove]
        del prices[remove]
        del quantity[amount]
        print('The item has been removed')            

    #compute total - WORKING    
    if choice2 == '4':
        total = sum(prices)
        print(f'Your total is ${"{:.2f}".format(total)}')

    #quits function - WORKING
    if choice2 == '5':
        quit = 1

print('Thank you. Goodbye.')
