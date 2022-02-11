import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Number is too low")
        elif guess > random_number:
            print("Sorry, guess again. Number is too high")
    print(f"Gz! You guessed correctly, {random_number} was the number!")

def computer_guess(x):
    low = 1
    high = x
    feedback =''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #or high, beacuse in this case low=high
        feedback = input(f'Is {guess} too high (H), Too low (L), or correct (C)?').lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess +1
    print(f"Computer guessed your number {guess} correctly!")


computer_guess(10)
