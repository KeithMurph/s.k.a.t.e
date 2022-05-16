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
bails = (' rolled their ankle!', ' creditcard themselves!', ' got a shinner!', ' fell on face', ' broke their board!', ' hit a rock!')
streak = 6
# function to check used tricks

# TODO
#  add turn based system
#  cpu vs player turn
#  cpu needs own stats for tricks
#  if cpu turn randomize trick that arent used on 'usedTricks' List
#  if trick is successful proceed
#  if unsuccessful switch turn to player
#  if player turn ask for trick
#  if trick is successful proceed

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
        game_active = False
        print('💀 You have lost sorry ', name)


# Introduction to the game
print('🛹 Welcome to the game of S.K.A.T.E!')
sleep(1)
print('💻 You will be playing against a computer.')
sleep(1)
print('please enter your name:')
name = input()
sleep(.5)
print(f"Welcome {name}" ,' goodluck!')
sleep(1)
print("The rules are simple match the computer's tricks and don't reach 'S.K.A.T.E'")

print("TRICKLIST: type 'list' to view during game"), print(trickDict)
sleep(1.5)

# Game loop
while game_active == True:

    # generate random trick and check if it has been used

    if currentTrick not in usedTricks:
        usedTricks.append(currentTrick)

    while currentTrick in usedTricks:
        currentTrick = random.choice(list(trickDict.keys()))

    sleep(1)
    print(f"{name}'s score:", skate)
    print(f"CPU Energy level:", streak)
    print()
    #  print(Fore.CYAN + 'cpu used tricklist: ', usedTricks[1:])
    print(f"💻 The computer did 🛹 {currentTrick}")
    print('enter trick:')


# trick input
    trickSelection = str.lower(input())


# end condition for game
    if trickSelection == 'exit':
        game_active = False

    if len(usedTricks) == len(trickDict):
        usedTricks.clear()

    if streak <= 1:
        print( ' You have worn put the computer you win!')
        game_active = False
# trick selections with odds

# ollie
    elif trickSelection == 'ol' or trickSelection == 'ollie':
        if random.choice(odds) >= 30:
            print(name +' landed an  OLLIE! 🛹')
            print()
            streak -= 1

        else:
            print(name + random.choice(bails))
            print()
            checkLetter()
            if skate == ['S', 'K', 'A', 'T', 'E']:
                game_active = False


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


# frontside shuvit
    elif trickSelection == 'fssh' or trickSelection == 'fs shuvit':
        if random.choice(odds) >= 45:
            print(name + ' Landed a Frontside Shuv! 🛹')
            print()
            streak -= 1

        else:
            print(name+ random.choice(bails))
            print()
            checkLetter()
            if skate == ['S', 'K', 'A', 'T', 'E']:
                game_active = False


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

        print(trickDict)
