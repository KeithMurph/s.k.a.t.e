import random
from time import sleep

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

<<<<<<< HEAD
# TODO
#  add turn based system
#  cpu vs player turn
#  cpu needs own stats for tricks
#  if cpu turn randomize trick that arent used on 'usedTricks' List
#  if trick is successful proceed
#  if unsuccessful switch turn to player
#  if player turn ask for trick
#  if trick is successful proceed
=======
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

>>>>>>> 2a66f23e1b9679225174800f84badffe59b7638f

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
print('🛹 Welcome to the game of S.K.A.T.E!')
sleep(1)
print('💻 You will be playing against PC')
sleep(1)
print('please enter your name:')
name = input()
sleep(.5)
print(f"Welcome {name}" ,' goodluck!')
sleep(1)
<<<<<<< HEAD
print("The rules are simple match the computer's tricks and don't reach 'S.K.A.T.E'")

print("TRICKLIST: type 'list' to view during game"), print(trickDict)
=======
print(Fore.CYAN + "The rules are simple match the computer's tricks and don't reach 'S.K.A.T.E'")

print(Fore.GREEN + "TRICKLIST:" + Fore.WHITE +" type 'list' to view during game"), print(Fore.YELLOW, trickDict)
>>>>>>> 2a66f23e1b9679225174800f84badffe59b7638f
sleep(1.5)

# Game loop
while game_active == True:

    # generate random trick and check if it has been used

    if currentTrick not in usedTricks:
        usedTricks.append(currentTrick)

    while currentTrick in usedTricks:
        currentTrick = random.choice(list(trickDict.keys()))

    sleep(1)
<<<<<<< HEAD
    print(f"{name}'s score:", skate)
    print(f"CPU Energy level:", streak)
    print()
    #  print(Fore.CYAN + 'cpu used tricklist: ', usedTricks[1:])
    print(f"💻 The computer did 🛹 {currentTrick}")
    print('enter trick:')
=======
    if skate != ['S', 'K', 'A', 'T', 'E']:
        print(Fore.GREEN + f"{name}'s score:", Fore.YELLOW, skate)
        print(Fore.GREEN + f"PC count down...", Fore.YELLOW, streak)
        print()
        #  print(Fore.CYAN + 'cpu used tricklist: ', usedTricks[1:])
        print(Fore.YELLOW + f"💻 PC did 🛹 {currentTrick}")
        print(Fore.GREEN + 'enter trick:')
>>>>>>> 2a66f23e1b9679225174800f84badffe59b7638f


# trick input
    trickSelection = str.lower(input())


# end condition for game
    if trickSelection == 'exit':
        game_active = False

    if len(usedTricks) == len(trickDict):
        usedTricks.clear()

<<<<<<< HEAD
    if streak <= 1:
        print( ' You have worn put the computer you win!')
        game_active = False
=======
    
>>>>>>> 2a66f23e1b9679225174800f84badffe59b7638f
# trick selections with odds
    elif skate == ['S', 'K', 'A', 'T', 'E']:
        game_active = False
# ollie
<<<<<<< HEAD
    elif trickSelection == 'ol' or trickSelection == 'ollie':
        if random.choice(odds) >= 30:
            print(name +' landed an  OLLIE! 🛹')
            print()
            streak -= 1
=======
    if currentTrick == 'OLLIE':
        if trickSelection == 'ol' or trickSelection == 'ollie':
            if random.choice(odds) >= 30:
                trickLand()
                streak -= 1
>>>>>>> 2a66f23e1b9679225174800f84badffe59b7638f

            else:
                trickBail()
                checkLetter()
                if skate == ['S', 'K', 'A', 'T', 'E']:
                    game_active = False
        else:
<<<<<<< HEAD
            print(name + random.choice(bails))
            print()
            checkLetter()
            if skate == ['S', 'K', 'A', 'T', 'E']:
                game_active = False
=======
            print(name + Fore.RED + ' flailed their board! 🛹')
            checkLetter()            
>>>>>>> 2a66f23e1b9679225174800f84badffe59b7638f

    # kickflip
    if currentTrick == 'KICKFLIP':
        if trickSelection == 'kf' or trickSelection == 'kickflip':
            if random.choice(odds) >= 55:
                trickLand()
                streak -= 1

<<<<<<< HEAD
# kickflip
    elif trickSelection == 'kf' or trickSelection == 'kickflip':
        if random.choice(odds) >= 55:
            print(name + ' Landed a KICKFLIP! 🛹')
            print()
            streak -= 1

        else:
            print(name +random.choice(bails))
            print()
            checkLetter()
            if skate == ['S', 'K', 'A', 'T', 'E']:
                game_active = False
=======
            else:
                trickBail()
                checkLetter()
                if skate == ['S', 'K', 'A', 'T', 'E']:
                    game_active = False
        else:
            print(name + Fore.RED + ' flailed their board! 🛹')
            checkLetter()            
>>>>>>> 2a66f23e1b9679225174800f84badffe59b7638f

    # heelflip
    if currentTrick == 'HEELFLIP':
        if trickSelection == 'hf' or trickSelection == 'heelflip':
            if random.choice(odds) >= 60:
                trickLand()
                streak -= 1

<<<<<<< HEAD
# heelflip
    elif trickSelection == 'hf' or trickSelection == 'heelflip':
        if random.choice(odds) >= 60:
            print(name + ' Landed a HEELFLIP! 🛹')
            print()
            streak -= 1

        else:
            print(name + random.choice(bails))
            print()
            checkLetter()
            if skate == ['S', 'K', 'A', 'T', 'E']:
                game_active = False
=======
            else:
                trickBail()
                checkLetter()
                if skate == ['S', 'K', 'A', 'T', 'E']:
                    game_active = False
        else:
            print(name + Fore.RED + ' flailed their board! 🛹')
            checkLetter()            
>>>>>>> 2a66f23e1b9679225174800f84badffe59b7638f

    # backside shuvit
    if currentTrick == 'BS SHUVIT':
        if trickSelection == 'bssh' or trickSelection == 'bs shuv':
            if random.choice(odds) >= 40:
                trickLand()
                streak -= 1

<<<<<<< HEAD
# backside shuvit
    elif trickSelection == 'bssh' or trickSelection == 'bs shuv':
        if random.choice(odds) >= 40:
            print(name + ' Landed a Backside Shuv! 🛹')
            print()
            streak -= 1

        else:
            print(name+ random.choice(bails))
            print()
            checkLetter()
            if skate == ['S', 'K', 'A', 'T', 'E']:
                game_active = False
=======
            else:
                trickBail()
                checkLetter()
                if skate == ['S', 'K', 'A', 'T', 'E']:
                    game_active = False
        else:
            print(name + Fore.RED + ' flailed their board! 🛹')
            checkLetter()            
>>>>>>> 2a66f23e1b9679225174800f84badffe59b7638f

    # frontside shuvit
    if currentTrick == 'FS SHUVIT':

<<<<<<< HEAD
# frontside shuvit
    elif trickSelection == 'fssh' or trickSelection == 'fs shuvit':
        if random.choice(odds) >= 45:
            print(name + ' Landed a Frontside Shuv! 🛹')
            print()
            streak -= 1
=======
        if trickSelection == 'fssh' or trickSelection == 'fs shuvit':
            if random.choice(odds) >= 45:
                trickLand()
                streak -= 1
>>>>>>> 2a66f23e1b9679225174800f84badffe59b7638f

            else:
                trickBail()
                checkLetter()
                if skate == ['S', 'K', 'A', 'T', 'E']:
                    game_active = False
        else:
<<<<<<< HEAD
            print(name+ random.choice(bails))
            print()
            checkLetter()
            if skate == ['S', 'K', 'A', 'T', 'E']:
                game_active = False
=======
            print(name + Fore.RED + ' flailed their board! 🛹')
            checkLetter()            
>>>>>>> 2a66f23e1b9679225174800f84badffe59b7638f

    # frontside 180
    if currentTrick == 'FS 180':
        if trickSelection == 'fs180' or trickSelection == 'fs 180':
            if random.choice(odds) >= 50:
                trickLand()
                streak -= 1

<<<<<<< HEAD
# frontside 180
    elif trickSelection == 'fs180' or trickSelection == 'fs 180':
        if random.choice(odds) >= 50:
            print(name + ' Landed Frontside 180! 🛹')
            print()
            streak -= 1

        else:
            print(name + random.choice(bails))
            print()
            checkLetter()
            if skate == ['S', 'K', 'A', 'T', 'E']:
                game_active = False
=======
            else:
                trickBail()
                checkLetter()
                if skate == ['S', 'K', 'A', 'T', 'E']:
                    game_active = False
        else:
            print(name + Fore.RED + ' flailed their board! 🛹')
            checkLetter()            
>>>>>>> 2a66f23e1b9679225174800f84badffe59b7638f

    # backside 180
    if currentTrick == 'BS 180':
        if trickSelection == 'bs180' or trickSelection == 'bs 180':
            if random.choice(odds) >= 50:
                trickLand()
                streak -= 1

<<<<<<< HEAD
# backside 180
    elif trickSelection == 'bs180' or trickSelection == 'bs 180':
        if random.choice(odds) >= 50:
            print(name + ' Landed a Backside 180! 🛹')
            print()
            streak -= 1

        else:
            print(name +random.choice(bails))
            print()
            checkLetter()
            if skate == ['S', 'K', 'A', 'T', 'E']:
                game_active = False
=======
            else:
                trickBail()
                checkLetter()
                if skate == ['S', 'K', 'A', 'T', 'E']:
                    game_active = False
        else:
            print(name + Fore.RED + ' flailed their board! 🛹')
            checkLetter()            
>>>>>>> 2a66f23e1b9679225174800f84badffe59b7638f

    # treflip
    if currentTrick == 'TREFLIP':
        if trickSelection == 'tre' or trickSelection == 'treflip':
            if random.choice(odds) >= 75:
                trickLand()
                streak -= 1

<<<<<<< HEAD
# treflip
    elif trickSelection == 'tre' or trickSelection == 'treflip':
        if random.choice(odds) >= 75:
            print(name + ' Landed a TREFLIP! 🛹')
            print()
            streak -= 1

        else:
            print(name + random.choice(bails))
            print()
            checkLetter()
            if skate == ['S', 'K', 'A', 'T', 'E']:
                game_active = False
# list
    elif trickSelection == 'list':
        print("TRICKLIST:"), print( trickDict)

# else condition
    else:
        print(name + ' flailed their board! 🛹')
        checkLetter()
=======
            else:
                trickBail()
                checkLetter()
                if skate == ['S', 'K', 'A', 'T', 'E']:
                    game_active = False     
#else condition for bail  
        else:
            print(name + Fore.RED + ' flailed their board! 🛹')
            checkLetter()
    # win condition for player
    if streak == 0: 
            print(streak)
            print(Fore.GREEN + 'PC got tired and walked away...')
            sleep(3)
            print('you win')
            sleep(1)
            print('I guess')
            game_active = False

>>>>>>> 2a66f23e1b9679225174800f84badffe59b7638f

