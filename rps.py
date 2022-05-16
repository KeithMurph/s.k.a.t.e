import random
from time import sleep
options = ['r', 'p', 's']

print('Lets play!')
sleep(1)
print('We Play Rock Paper Scissors to see who goes first!')
print('Please enter your name:')
name = input()
cpuTurn = True
sleep(1)
print(f'Welcome {name}!')



print('Please enter your choice:')

choice = input()
print(f'{name} chose {choice}')
print('...')
sleep(1.2)
print('Computer chose:')
computer_choice = random.choice(options)
print(computer_choice)
if choice == computer_choice:
    print('It is a tie PC goes first!')
elif choice == 'r' and computer_choice == 's':
    print('You go first!')
    cpuTurn = False
elif choice == 'r' and computer_choice == 'p':
    print('PC goes first!')
elif choice == 'p' and computer_choice == 'r':
    print('You go first!')
    cpuTurn = False
elif choice == 'p' and computer_choice == 's':
    print('PC goes first!')
elif choice == 's' and computer_choice == 'p':
    print('You go first!')
    cpuTurn = False
elif choice == 's' and computer_choice == 'r':
    print('PC goes first!')
else:
    print('Invalid choice PC goes first!')


