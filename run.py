import random
from words import word_list
import string
from colored import fg
import pygame

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
UNDERLINE = '\033[4m'
RESET = '\033[0m'

print("Welcome to the Hangman Game!")
print("Do you know the rules?")
print("(1)Yes, take me to the game.\n(2)No, show me the rules.")

def intro():
    """
    Function to determine action after user choice.
    Either user beginnes the game without further informations, or he gets to know the rules.
    If inncorect number is chosen it asks user to repet the action.
    """
    user_choice1 = input("-> \n")
    for num in user_choice1:    
        if (user_choice1 == '1'):
            print("This is where the fun begins!\n")
            game(gameword)
        elif (user_choice1 == '2'):
            print("\n")
            print("GAME RULES:")
            print("-> You have to guess the secret word before the stick figure is hung.")
            print("-> The computer will indicate how many letters is in the word. One letter = '_'.")
            print("-> You have six chances to guess the word.")
            print("-> If you choose the letter, that letter will be delited from the list. ")
            print("-> You have 3 warnings: you lose one warning each time if you chose a letter which has been already used or symbols which are not letters  ")
            print("\n")
            print("Are you ready now to begin the game?")
            print("(1)Yes, take me to the game.\n(2)No, exit the game.")
            wrong_choice()  
        else:
            print(RED + "Incorrect number, please enter your choice again." + WHITE)
        intro()

def wrong_choice(): 
    """
    Function to loop over user choice until he choses correct number to either start the game or exit the game
    """
    user_choice2 = input("-> ")
    for num in user_choice2:
        if (user_choice2 == '1'):
            game(gameword)
        elif (user_choice2 == '2'):
            print('THE END')
            exit()
        else:
            print(RED + "Incorrect number, please enter your choice again." + WHITE)
        wrong_choice()


def get_word():
    """
    Function to pull out guess word for the user from the word_list
    """
    word = random.choice(word_list)
    return word.upper()


def is_word_guessed(gameword, letters_already_guessed):
    """
    Function to compare letters pickes by a user to letters contained in guess word
    If letters in word are equal to letters picked by a user return True and 'do stomething' otherwise return False
    and 'do something'
    """
    if set(gameword) & set(letters_already_guessed) == set(gameword):
        return True
    else:
        return False

def show_guessed_word(gameword, letters_already_guessed):
    """
    Show to user the gameword by displaying number of '_' equivalent to length of the word
    Allow user to see the number of guessed letters and remaining letters that are needed to be guessed.
    """
    result_list = []
    for i in range(len(gameword)):
        if list(gameword)[i] in set(letters_already_guessed):
            result_list.append(list(gameword)[i])
        else:
            result_list.append("_ ")
    return ''.join(map(str, result_list))

def available_letters(letters_already_guessed):
    """
    Function to return alphabet letter without letters which has been picked by the user
    User can see what letters are still available to pick 
    To avoid choosing the same letters
    """
    still_available = list(string.ascii_uppercase)

    for i in range(-len(still_available), 0):
        if still_available[i] in letters_already_guessed:
            still_available.remove(still_available[i])
    return  ' '.join(still_available)
            
def game(gameword):
    """
    Function to implement the body of the program and
    Use previouse functions whitin this body
    Determine user choices scenario
    """
    used_letters = []
    guessed = False
    guesses_remaining = 6
    warnings_remaining = 3
    print('The game is loading...\n')
    print('A gameword is', len(gameword), 'letters long.\n')

    while not guessed and guesses_remaining > 0:
        """
        Decrease user remaining guesses and warning each time letter is entered by user 
        If incorrect sign or repeating previusly picked letter is entered user looses 1 warning
        """
        if not is_word_guessed(gameword, used_letters):
           
            print('You have', int(guesses_remaining), "guess(es) left and", int(warnings_remaining), 'warning(s) left!','\n')
            print("Available letters: ", available_letters(used_letters),'\n')
            
            guess = input('Please enter letter of your choice:  \n').upper()

            if guessed == False:
                guesses_remaining -= 1
                if not guess.isalpha(): 
                    warnings_remaining -= 1
                    print(RED + 'Inncorect entry, you loose 1 warning!\n' + WHITE)








gameword = get_word()
start = intro()

   

