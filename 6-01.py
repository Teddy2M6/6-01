import random

def number_picker():

    user = 'y'

    while (user == 'y'):

        numbers = [1, 2, 3, 4, 5, 6]

        user = int(input('Enter a number between 1 and 6: '))
        print()

        if (user >= 7):
            print(int(input('Please enter a number between 1 and 6: ')))

        for i in range(1):
            ran = random.choice(numbers)
            print('The number was', ran)
            
number_picker()
