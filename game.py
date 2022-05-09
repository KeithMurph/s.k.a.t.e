import random
from time import sleep
from colorama import init, Fore, Back, Style

# tricklist
trickDict = {'OLLIE': 'ol', 'KICKFLIP': 'kf', 'HEELFLIP': 'hf', 'BS SHUVIT': 'bssh','FS SHUVIT': 'fssh', 'FS 180': 'fs180', 'BS 180': 'bs180', 'TREFLIP': 'tre'}
odds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
        51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# game score s.k.a.t.e
skate = []
usedTricks = []
currentTrick = ''
game_active = True
bails = (' rolled their ankle!', ' creditcard themselves!',' got a shinner!', ' just sucks', ' fell on face', ' broke their board!', ' hit a rock!')
skatjectives = (' POPPED a ', ' barely landed ', ' snapped a BIG OL ', ' landed a ', ' did a sketchy ')
streak = 6
# function to check used tricks

# functions trick makes and bails


def trickLand():
    print('...')
    sleep(0.5)
    print(Fore.CYAN + name + Fore.YELLOW + random.choice(skatjectives) + currentTrick + ' 🛹')
    print()


def trickBail():
    print('...')
    sleep(.5)
    print(name + Fore.RED + random.choice(bails))
    print()


# function to check current letter
def checkLetter():
    if skate == []:
        skate.append('S')
    elif skate == ['S']:
        skate.append('K')
    elif skate == ['S', 'K']:
        skate.append('A')
    elif skate == ['S', 'K', 'A']:
        skate.append('T')
    elif skate == ['S', 'K', 'A', 'T']:
        skate.append('E')
        print(skate)
        game_active == False
        print(name, '💀 You have lost!!')
        print()


# Introduction to the game
print(Fore.GREEN + '🛹 Welcome to the game of S.K.A.T.E!')
sleep(1)
print('💻 You will be playing against a computer.')
sleep(1)
print('please enter your name:')
name = input(Fore.YELLOW)
sleep(.5)
print(f"Welcome {Fore.GREEN + name}" + Fore.YELLOW + ' goodluck!')
sleep(1)
print(Fore.CYAN + "The rules are simple match the computer's tricks and don't reach 'S.K.A.T.E'")

print(Fore.GREEN + "TRICKLIST:" + Fore.WHITE +" type 'list' to view during game"), print(Fore.YELLOW, trickDict)
sleep(1.5)

# Game loop
while game_active == True:

    # generate random trick and check if it has been used

    if currentTrick not in usedTricks:
        usedTricks.append(currentTrick)

    while currentTrick in usedTricks:
        currentTrick = random.choice(list(trickDict.keys()))

    sleep(1)
    if skate != ['S', 'K', 'A', 'T', 'E']:
        print(Fore.GREEN + f"{name}'s score:", Fore.YELLOW, skate)
        print(Fore.GREEN + f"CPU count down...", Fore.YELLOW, streak)
        print()
        #  print(Fore.CYAN + 'cpu used tricklist: ', usedTricks[1:])
        print(Fore.YELLOW + f"💻 The computer did 🛹 {currentTrick}")
        print(Fore.GREEN + 'enter trick:')


# trick input
    trickSelection = str.lower(input(Fore.YELLOW))


# end condition for game
    if trickSelection == 'exit':
        game_active = False

    if len(usedTricks) == len(trickDict):
        usedTricks.clear()

    
# trick selections with odds
    elif skate == ['S', 'K', 'A', 'T', 'E']:
        game_active = False
# ollie
    if currentTrick == 'OLLIE':
        if trickSelection == 'ol' or trickSelection == 'ollie':
            if random.choice(odds) >= 30:
                trickLand()
                streak -= 1

            else:
                trickBail()
                checkLetter()
                if skate == ['S', 'K', 'A', 'T', 'E']:
                    game_active = False
        else:
            print(name + Fore.RED + ' flailed their board! 🛹')
            checkLetter()            

    # kickflip
    if currentTrick == 'KICKFLIP':
        if trickSelection == 'kf' or trickSelection == 'kickflip':
            if random.choice(odds) >= 55:
                trickLand()
                streak -= 1

            else:
                trickBail()
                checkLetter()
                if skate == ['S', 'K', 'A', 'T', 'E']:
                    game_active = False
        else:
            print(name + Fore.RED + ' flailed their board! 🛹')
            checkLetter()            

    # heelflip
    if currentTrick == 'HEELFLIP':
        if trickSelection == 'hf' or trickSelection == 'heelflip':
            if random.choice(odds) >= 60:
                trickLand()
                streak -= 1

            else:
                trickBail()
                checkLetter()
                if skate == ['S', 'K', 'A', 'T', 'E']:
                    game_active = False
        else:
            print(name + Fore.RED + ' flailed their board! 🛹')
            checkLetter()            

    # backside shuvit
    if currentTrick == 'BS SHUVIT':
        if trickSelection == 'bssh' or trickSelection == 'bs shuv':
            if random.choice(odds) >= 40:
                trickLand()
                streak -= 1

            else:
                trickBail()
                checkLetter()
                if skate == ['S', 'K', 'A', 'T', 'E']:
                    game_active = False
        else:
            print(name + Fore.RED + ' flailed their board! 🛹')
            checkLetter()            

    # frontside shuvit
    if currentTrick == 'FS SHUVIT':

        if trickSelection == 'fssh' or trickSelection == 'fs shuvit':
            if random.choice(odds) >= 45:
                trickLand()
                streak -= 1

            else:
                trickBail()
                checkLetter()
                if skate == ['S', 'K', 'A', 'T', 'E']:
                    game_active = False
        else:
            print(name + Fore.RED + ' flailed their board! 🛹')
            checkLetter()            

    # frontside 180
    if currentTrick == 'FS 180':
        if trickSelection == 'fs180' or trickSelection == 'fs 180':
            if random.choice(odds) >= 50:
                trickLand()
                streak -= 1

            else:
                trickBail()
                checkLetter()
                if skate == ['S', 'K', 'A', 'T', 'E']:
                    game_active = False
        else:
            print(name + Fore.RED + ' flailed their board! 🛹')
            checkLetter()            

    # backside 180
    if currentTrick == 'BS 180':
        if trickSelection == 'bs180' or trickSelection == 'bs 180':
            if random.choice(odds) >= 50:
                trickLand()
                streak -= 1

            else:
                trickBail()
                checkLetter()
                if skate == ['S', 'K', 'A', 'T', 'E']:
                    game_active = False
        else:
            print(name + Fore.RED + ' flailed their board! 🛹')
            checkLetter()            

    # treflip
    if currentTrick == 'TREFLIP':
        if trickSelection == 'tre' or trickSelection == 'treflip':
            if random.choice(odds) >= 75:
                trickLand()
                streak -= 1

            else:
                trickBail()
                checkLetter()
                if skate == ['S', 'K', 'A', 'T', 'E']:
                    game_active = False          
        else:
            print(name + Fore.RED + ' flailed their board! 🛹')
            checkLetter()
    if streak == 0: 
            print(streak)
            print(Fore.GREEN + ' You have worn put the computer you win!')
            game_active = False


