import random
print("Welcome To The Number Guessing Game!\nChoose A Number Between 1 And 9")
inp = int(input("Enter A Number : "))
ranNum = random.randint(1, 9)
chances = 5

while chances > 0:
    if inp > ranNum:
        print("Oh No! Guess Lower")
    elif inp < ranNum:
        print("Oh No! Guess Higher")
    elif inp == ranNum:
        print('Congratulations! You Got It')
        break
    else:
        print('Invalid Input')
    chances -= 1
    inp = int(input('Enter A Number : '))

if chances == 0:
    print('You Lose!\nThe Number Is ' + str(ranNum))