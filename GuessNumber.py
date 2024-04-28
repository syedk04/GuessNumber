import random #imports random which allows code to use anything within random

def guess(x): #function is defined using def
    random_number = random.randint(1, x) #random number is found using random.randint
    guess = 0 # can never be zero
    while guess != random_number: 
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number: #run if statement if too high
            print('Guess again, too low!')
        elif guess > random_number: #run else if, if too low
            print('Guess again, too high!')
    
    print(f'Congrats, you have guessed the correct number {random_number}')

guess(30)
