#under 36 in can't ride
#single rider must be 18 y/o and 62 in tall
#2 riders one must be 18

#person 1 height and age
age1 = float(input('What is the age of the first rider? '))
height1 = float(input('What is the height of the first rider? '))

#2 people?
rider2 = input('Is there a second rider? (yes/no)? ')

#person 2 age and height
if rider2 == 'yes':
    rider2 = True
    age2 = float(input('What is the age of the second rider? '))
    height2 = float(input('What is the height of the second rider? '))
elif rider2 == 'no':
    rider2 = False
    height2 = 100
    age2 = 100

#golden passport
passport1 = input('Does the first rider have a golden passport? (y/n) ')
if passport1 == 'y':
    passport1 == True
else: 
    passport1 == False

if rider2 == True:
    passport2 = input('Does the second rider have a golden passport? (y/n) ')
    if passport2 == 'y':
        passport2 == True
    else: 
        passport2 == False

#disposition
if height1 < 36 or height2 < 36:    #too short
    print('Sorry, you may not ride.')
elif rider2 == False:     #1 rider
    if age1 >= 18 and height1 >= 62:
        print('Welcome to the ride. Please be safe and have fun.')
    else:
        print('Sorry, you may not ride.')
elif rider2 == True:      #2 rider age req
    if age1 >=18 or age2 >= 18:
        print('Welcome to the ride. Please be safe and have fun.')
    else:
        print('Sorry, you may not ride.')
elif rider2 == True:      #2 riders but young
    if age1 >= 12 and age2 >= 12 and height1 >=62 and height2 >= 62:
        print('Welcome to the ride. Please be safe and have fun.')
elif passport1 == True:   #golden passport conditional
    if height1 >= 62:
        print('Welcome to the ride. Please be safe and have fun.')
    elif passport1 == False:
        if passport2 == True:
            print('Welcome to the ride. Please be safe and have fun.')
elif age1 >= 16 or age2 >= 16 and age1 >= 14 or age2 >= 14:
    print('Welcome to the ride. Please be safe and have fun.')
else:
    print('Sorry, you may not ride.')