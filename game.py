import random 
from time import sleep
from colorama import init, Fore, Back, Style

# tricklist
trickDict = {'ol': 'OLLIE', 'kf': 'KICKFLIP', 'hf': 'HEELFLIP', 'bssh': 'BS SHUV', 'fssh': 'FS SHUV', 'fs180': 'FS 180', 'bs180': 'BS 180', 'tre': 'TREFLIP'}
odds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# game score s.k.a.t.e
skate = []
usedTricks = []
currentTrick = ''
game_active = True
bails = ('rolled their ankle!', 'creditcard themselves!', 'got a shinner!', 'fell on face', ' broke their board!', 'hit a rock!')

# function to check used tricks


# function to check current letter
def checkLetter():
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
        print('💀 You have lost sorry ', name)
        game_active = False
        
    
# Introduction to the game
print(Fore.GREEN + '🛹 Welcome to the game of S.K.A.T.E!')
sleep(1)
print('💻 You will be playing against a computer.')
sleep(1)
print('please enter your name:')
name = input(Fore.YELLOW)
sleep(.5)
print(f"Hello {Fore.GREEN + name}")
sleep(1)
print(Fore.YELLOW + "The rules are simple match the computer's tricks and don't reach 'S.K.A.T.E'")
print(Fore.LIGHTWHITE_EX, trickDict)
sleep(1.5)

# Game loop
while game_active == True:

    

    # generate random trick and check if it has been used
    
    if currentTrick not in usedTricks:
            usedTricks.append(currentTrick)
        
        
    while currentTrick in usedTricks:
        currentTrick = random.choice(list(trickDict.values()))


    sleep(1)
    print(Fore.CYAN + f"{name}'s score:" , Fore.YELLOW, skate)
    #  print(Fore.CYAN + 'cpu used tricklist: ', usedTricks[1:])
    print(Fore.YELLOW + f"The computer did 🛹 {currentTrick}")
    print(Fore.GREEN + 'enter trick:')


# trick input
    trickSelection = str.lower(input(Fore.YELLOW))
    


# end condition for game
    if trickSelection == 'exit':
        game_active = False

    if len(usedTricks) == len(trickDict):
       usedTricks.clear()

# trick selections with odds

# ollie
    elif trickSelection == 'ol' or trickSelection == 'ollie':
        if random.choice(odds) >= 30:
            print(name+ Fore.GREEN + 'landed an  OLLIE! 🛹')

        else:
            print(name+ Fore.RED + random.choice(bails))
            checkLetter()  
            if skate == ['S', 'K', 'A', 'T', 'E']:
                game_active = False
           

# kickflip
    elif trickSelection == 'kf' or trickSelection == 'kickflip':
        if random.choice(odds) >= 55:
            print(name+ Fore.GREEN + 'Landed a KICKFLIP! 🛹')

        else:
            print(name + Fore.RED + random.choice(bails))
            checkLetter()
            if skate == ['S', 'K', 'A', 'T', 'E']:
                game_active = False
            

# heelflip
    elif trickSelection == 'hf' or trickSelection == 'heelflip':
        if random.choice(odds) >= 60:
            print(name+ Fore.GREEN + 'Landed a HEELFLIP! 🛹')

        else:
            print(name+ Fore.RED + random.choice(bails))
            checkLetter()
            if skate == ['S', 'K', 'A', 'T', 'E']:
                game_active = False
            


# backside shuvit
    elif trickSelection == 'bssh' or trickSelection == 'bs shuv':
        if random.choice(odds) >= 40:
            print(name +Fore.GREEN + 'Landed a Backside Shuv! 🛹')

        else:
            print(name +Fore.RED + random.choice(bails))
            checkLetter()
            if skate == ['S', 'K', 'A', 'T', 'E']:
                game_active = False
           


# frontside shuvit
    elif trickSelection == 'fssh' or trickSelection == 'fs shuvit':
        if random.choice(odds) >= 45:
            print(name+ Fore.GREEN + 'Landed a Frontside Shuv! 🛹')

        else:
            print(name+ Fore.RED + random.choice(bails))
            checkLetter() 
            if skate == ['S', 'K', 'A', 'T', 'E']:
                game_active = False 
            


# frontside 180
    elif trickSelection == 'fs180' or trickSelection == 'fs 180':
        if random.choice(odds) >= 50:
            print(name+ Fore.GREEN + 'Landed Frontside 180! 🛹')

        else:
            print(name+ Fore.RED + random.choice(bails))
            checkLetter()
            if skate == ['S', 'K', 'A', 'T', 'E']:
                game_active = False
                                         


# backside 180
    elif trickSelection == 'bs180' or trickSelection == 'bs 180':
        if random.choice(odds) >= 50:
            print(name+ Fore.GREEN + 'Landed a Backside 180! 🛹')

        else:
            print(name+ Fore.RED + random.choice(bails))
            checkLetter() 
            if skate == ['S', 'K', 'A', 'T', 'E']:
                game_active = False
            

# treflip
    elif trickSelection == 'tre' or trickSelection == 'treflip':
        if random.choice(odds) >= 75:
            print(name + Fore.GREEN + 'Landed a TREFLIP! 🛹')

        else:
            print(name+ Fore.RED + random.choice(bails))
            checkLetter() 
            if skate == ['S', 'K', 'A', 'T', 'E']:
                game_active = False
            
    else:
        checkLetter()
        
        print(trickDict)