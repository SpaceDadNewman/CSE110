numbers = []
number = None
total = 0
count = 0

print('Type a list of numbers, type 0 when finished.')
while number != 0:
    number = int(input('Enter number: '))
    total += number
    count += 1
    numbers.append(number)

newnumbers = sorted(numbers)
average = total / count

print(f'The sum is: {total}')
print(f'The average is {average}')
print(f'The largest number is: ', max(numbers))
print(f'The smallest positive number is: ', min([number for number in numbers if number > 0]))
print('The sorted list is: ')
for number in newnumbers:
    print(number)