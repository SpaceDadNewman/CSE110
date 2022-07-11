import random

count = 0
number = random.randint(1, 10)

guess = float(input('What is your guess? '))

while guess != number:
    if guess < number:
        print('Higher')
    elif guess > number:
        print('Lower')
    guess = float(input('What is your guess? '))
    count += 1

print('You guessed it!')
print(f'You guessed {count} times')