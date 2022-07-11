print('Please enter the following:\n')

#prompt
adj1 = input('Adjective: ')
adj2 = input('Adjective: ')
noun = input('Noun: ')
name1 = input('Someone\'s full name: ')
car = input('Type of Car: ')
adj3 = input('Adjective: ')
adj4 = input('Adjective: ')
name2 = input('First name: ')
gender = input('Gender of second name (man/woman): ')
adj5 = input('Adjective: ')
pverb = input('Past tense verb: ')
noun2 = input('Noun: ')

print('\nYour story is:\n')

#story
print(f'A {adj1}, {adj2}, {noun}\n\
named {name1.title()} sold their {car.title()} \n\
to a {adj3} and {adj4} {gender} \n\
named {name2.title()}. This is shaping \n\
up to be an {adj5} day for {name2.title()}.\n\
Later, {name2.title()} {pverb} the {car.title()}\n\
and flipped the car for {noun2}.')