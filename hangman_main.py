import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) 
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()
def hangman(): 
    word = get_valid_word(words)
    word_letters = set(word) #letters in a word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #What the user has guessed

    lives = 10

    #Getting user input
    while len(word_letters) > 0 and lives > 0 :
        #letters used
        #.join('a', 'b', 'cd') --> 'a b cd' 
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        #What is your current word in the format of 'P - T - O N'
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter is not in the word')
        
        elif user_letter in used_letters:
            print('That character was used already. Try another one')
        
        else:
            print('Invalid character. Try again')

    # Gets here if len(word_letters) == 0 or lives == 0
    if lives == 0:
        print('You died! Better luck next time! The word was ', word)
    else:
        print('You guessed the word', word, '!','','Good Job!')

hangman ()
