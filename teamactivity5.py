grade = float(input('What is your grade in class? '))

if grade > 93:
    letter = 'A'
elif grade >= 90:
    letter = 'A-'
elif grade >= 87:
    letter = 'B+'
elif grade > 83:
    letter = 'B'
elif grade >= 80:
    letter = 'B'
elif grade >= 77:
    letter = 'C+'
elif grade > 73:
    letter = 'C'
elif grade >= 70:
    letter = 'C-'
elif grade >= 67:
    letter = 'D+'
elif grade > 63:
    letter = 'D'
elif grade >= 60:
    letter = 'D-'
else:
    letter = 'F'

print(f'You have a {letter} in this class')
if grade >= 70:
    print('Good job! U done good kid.')
else:
    print('Cheer up champ, do better.')
