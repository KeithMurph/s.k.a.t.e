import random 
from time import sleep
from colorama import init, Fore, Back, Style

# tricklist
trickDict = {'ol': 'ollie', 'kf': 'kickflip', 'hf': 'heelflip', 'bssh': 'backside shuvit', 'fssh': 'frontside shuvit', 'tre': 'treflip', 'fs180': 'frontside 180', 'bs180': 'backside 180' }
odds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
skate = []
game_active = True


# Introduction to the game
name = input(Fore.YELLOW + "What is your name? ")
sleep(.5)
print(Fore.CYAN + f"Hello {Fore.GREEN + name}", Fore.CYAN + "Welcome to the game of SKATE")
sleep(2)
print(Fore.YELLOW + "The rules are simple match the computer's tricks to win!")
print(Fore.WHITE, trickDict)
sleep(3)

# Game loop
while game_active == True:
    currentTrick = random.choice(list(trickDict.values()))
    
    sleep(1)
    print(name,"'s score:" , Fore.GREEN, skate)
    print(Fore.CYAN + f"The computer has chosen {currentTrick}")
    print(Fore.YELLOW + 'enter trick:')
    trickSelection = input()
    

# end condition for game
    if trickSelection == 'exit':
        game_active = False

# trick selections with odds

# ollie
    elif trickSelection == 'ol':
        if random.choice(odds) >= 30:
            print(Fore.GREEN + 'OLLIE! 🛹')

        else:
            print(Fore.RED + 'slipped and fell!')
            if skate == []:
                skate.append('S')
                print(skate)
            elif skate == ['S']:
                skate.append('K')
                print(skate)
            elif skate == ['S', 'K']:
                skate.append('A')
                print(skate)
            elif skate == ['S', 'K', 'A']:
                skate.append('T')
                print(skate)
            elif skate == ['S', 'K', 'A', 'T']:
                skate.append('E')
                print(skate)
                print('You Lost!')
                game_active = False

# kickflip
    elif trickSelection == 'kf':
        if random.choice(odds) >= 40:
            print(Fore.GREEN + 'KICKFLIP! 🛹')

        else:
            print(Fore.RED + 'rolled ankle!')
            if skate == []:
                skate.append('S')
                print(skate)
            elif skate == ['S']:
                skate.append('K')
                print(skate)
            elif skate == ['S', 'K']:
                skate.append('A')
                print(skate)
            elif skate == ['S', 'K', 'A']:
                skate.append('T')
                print(skate)
            elif skate == ['S', 'K', 'A', 'T']:
                skate.append('E')
                print(skate)
                print('You Lost!')
                game_active = False


# heelflip
    elif trickSelection == 'hf':
        if random.choice(odds) >= 60:
            print(Fore.GREEN + 'HEELFLIP! 🛹')

        else:
            print(Fore.RED + 'CREDIT CARD!')
            if skate == []:
                skate.append('S')
                print(skate)
            elif skate == ['S']:
                skate.append('K')
                print(skate)
            elif skate == ['S', 'K']:
                skate.append('A')
                print(skate)
            elif skate == ['S', 'K', 'A']:
                skate.append('T')
                print(skate)
            elif skate == ['S', 'K', 'A', 'T']:
                skate.append('E')
                print(skate)
                print('You Lost!')
                game_active = False


# backside shuvit
    elif trickSelection == 'bssh':
        if random.choice(odds) >= 40:
            print(Fore.GREEN + 'Backside Shuv! 🛹')

        else:
            print(Fore.RED + 'SHINNER!')
            if skate == []:
                skate.append('S')
                print(skate)
            elif skate == ['S']:
                skate.append('K')
                print(skate)
            elif skate == ['S', 'K']:
                skate.append('A')
                print(skate)
            elif skate == ['S', 'K', 'A']:
                skate.append('T')
                print(skate)
            elif skate == ['S', 'K', 'A', 'T']:
                skate.append('E')
                print(skate)
                print('You Lost!')
                game_active = False


# frontside shuvit
    elif trickSelection == 'fssh':
        if random.choice(odds) >= 50:
            print(Fore.GREEN + 'Frontside Shuv! 🛹')

        else:
            print(Fore.RED + 'Fell on face!')
            if skate == []:
                skate.append('S')
                print(skate)
            elif skate == ['S']:
                skate.append('K')
                print(skate)
            elif skate == ['S', 'K']:
                skate.append('A')
                print(skate)
            elif skate == ['S', 'K', 'A']:
                skate.append('T')
                print(skate)
            elif skate == ['S', 'K', 'A', 'T']:
                skate.append('E')
                print(skate)
                print('You Lost!')
                game_active = False     


# frontside 180
    elif trickSelection == 'fs180':
        if random.choice(odds) >= 40:
            print(Fore.GREEN + 'Frontside 180! 🛹')

        else:
            print(Fore.RED + 'Fell on hip!')
            if skate == []:
                skate.append('S')
                print(skate)
            elif skate == ['S']:
                skate.append('K')
                print(skate)
            elif skate == ['S', 'K']:
                skate.append('A')
                print(skate)
            elif skate == ['S', 'K', 'A']:
                skate.append('T')
                print(skate)
            elif skate == ['S', 'K', 'A', 'T']:
                skate.append('E')
                print(skate)
                print('You Lost!')
                game_active = False                              


# backside 180
    elif trickSelection == 'bs180':
        if random.choice(odds) >= 60:
            print(Fore.GREEN + 'Backside 180! 🛹')

        else:
            print(Fore.RED + 'Fell on face!')
            if skate == []:
                skate.append('S')
                print(skate)
            elif skate == ['S']:
                skate.append('K')
                print(skate)
            elif skate == ['S', 'K']:
                skate.append('A')
                print(skate)
            elif skate == ['S', 'K', 'A']:
                skate.append('T')
                print(skate)
            elif skate == ['S', 'K', 'A', 'T']:
                skate.append('E')
                print(skate)
                print('You Lost!')
                game_active = False   

# treflip
    elif trickSelection == 'tre':
        if random.choice(odds) >= 70:
            print(Fore.GREEN + 'TREFLIP! 🛹')

        else:
            print(Fore.RED + 'ATE IT!')
            if skate == []:
                skate.append('S')
                print(skate)
            elif skate == ['S']:
                skate.append('K')
                print(skate)
            elif skate == ['S', 'K']:
                skate.append('A')
                print(skate)
            elif skate == ['S', 'K', 'A']:
                skate.append('T')
                print(skate)
            elif skate == ['S', 'K', 'A', 'T']:
                skate.append('E')
                print(skate)
                print('You Lost!')
                game_active = False   
    else:
        print('Invalid Input')
        print(trickDict)