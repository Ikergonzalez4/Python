import random 

def guess_the_number(x): 
    print('Welcome to Guess the Number!')
    print('Your goal is to guess the number I am thinking of.')

    random_number = random.randint(1, x)

    prediction = 0
    while prediction != random_number:
        prediction = int(input(f'Guess a number between 1 and {x}: '))
        if prediction < random_number:
            print('Sorry, guess again. Too low.')
        elif prediction > random_number:
            print('Sorry, guess again. Too high.')
    print(f'Congratulations! You guessed the number {random_number} correctly!')

guess_the_number(100)
