# [LAST NAME], [first name]
# [Job Title]
# ID: [id number]
# [email address]
# [phone number]
# [Hair]      [Eyes]
# [Month]     [Training y/n]

#gather
name_first = input('What is your first name?: ')
name_last = input('What is your last name?: ')
jtitle = input('What is your job title?: ')
id_num = input('What is your id number?: ')
email = input('What is your email address?: ')
phone = input('What is your phone number?: ')
hair = input('What is your hair color?: ')
eyes = input('What is your eye color?: ')
month = input('What month did you start?: ')
train = input('Have you completed the training? (yes/no): ')

#convert
print('The ID Card is:')
print('----------------------------------------')
print(f'{name_last.upper()}, {name_first.lower()}\n\
{jtitle.title()}\nID:{id_num}\n\n{email}\n\
{phone}')
print(f'Hair: {hair.title():<16} Eyes: {eyes.title()}')
print(f'Month: {month.title():<15} Training: {train.title()}')
print('----------------------------------------')
