import random
import pyfiglet
from words import word_list
import string
from colored import fg
import os


"""
Color variables to create user experience friendly colored text
"""
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
UNDERLINE = '\033[4m'
RESET = '\033[0m'

"""
Game logo with use of pyfiglet library
"""
result = pyfiglet.figlet_format("Hangman Game", font = "digital")
print(CYAN + result + RESET)

print(YELLOW + UNDERLINE  + "Welcome to the Hangman Game!" + RESET)
print("\n")
print(GREEN + "Do you know the rules?"+ RESET)
print("(1)Yes, take me to the game.\n(2)No, show me the rules.")

def intro():
    """
    Function to determine action after user choice.
    Either user beginnes the game without further informations, or he gets to know the rules.
    If inncorect number is chosen it asks user to repet the action.
    """
    user_choice1 = input("-> ")
    for num in user_choice1:    
        if (user_choice1 == '1'):
            print(YELLOW + "This is where the fun begins!\n" + RESET)
            os.system('cls||clear')
            game(gameword)
        elif (user_choice1 == '2'):
            print("\n")
            print(YELLOW + UNDERLINE + "GAME RULES:" + RESET)
            print("-> You have to guess the secret word before the stick figure is hung.")
            print("-> The computer will indicate how many letters is in the word.")
            print("-> One letter = '_'.")
            print("-> You have six chances to guess the word.")
            print("-> If you choose the letter, that letter will be delited from the list.")
            print("-> You have 3 warnings: you lose one warning each time if you chose a letter")
            print("   which has been already used or symbols which are not letters.")
            print("\n")
            print(YELLOW + UNDERLINE + "Are you ready now to begin the game?" + RESET)
            print("(1)Yes, take me to the game.\n(2)No, exit the game.")
            wrong_choice()  
        else:
            print(RED + "Incorrect number, please enter your choice again." + RESET)
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
            print("\n")
            print(RED + 'THE END'+ RESET)
            exit()
        else:
            print(RED + "Incorrect number, please enter your choice again." + RESET)
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
            still_available[i] = (RED + "x" + GREEN )
    return ' ' .join(still_available) 

       
            
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
    print('\n')

    while True:
        """
        Decrease user remaining guesses and warning each time letter is entered by user 
        If incorrect sign or repeating previusly picked letter is entered user is not losing guesses or wanrings
        If previously chosen letter is picked again, user looses 1 warning 
        """
        if not is_word_guessed(gameword, used_letters):
            print('You have', int(guesses_remaining), "guess(es) left and", int(warnings_remaining), 'warning(s) left!','\n')
            print(GREEN + "Available letters: ", available_letters(used_letters),'\n' + RESET)  
            print(display_hangman(guesses_remaining)) 
            guess = str.upper(input('Please enter letter of your choice: ')) 
            print('\n')  
               

            if guessed == False:
                
                if not guess.isalpha():
                    os.system('cls||clear')
                    print(RED + 'Oops! You pressed wrong key. Try again!\n' + RESET)
                    pass    
                elif len(str(guess)) != 1:
                    os.system('cls||clear')
                    print(RED + 'Oops! You pressed the same letter multiple times. Try again!\n' + RESET)
                    pass
                elif guess in used_letters:
                    os.system('cls||clear')
                    warnings_remaining -= 1
                    print(RED + 'This letter has already been used, you lose 1 warning!\n' + RESET)
                    print(display_hangman(guesses_remaining))
                    if warnings_remaining == 0:
                        os.system('cls||clear')
                        print(RED + 'You run out of warning! This is the end of the game! Good luck next time!\n'+ RESET)
                        exit()
                elif guess in set(gameword):
                    os.system('cls||clear')
                    print(YELLOW + 'You got it right!' + RESET)
                    used_letters.append(guess)                
                    guesses_remaining -= 1
                    press = input(YELLOW +'Press any key to continue.\n' + RESET)
                    

                elif guesses_remaining <= 0:
                    os.system('cls||clear')
                    print(RED + 'Sorry, you have no more guesses available. The word was: \n'+ RESET, gameword)
                    print(RED+ 'THE END' + RESET)
                    exit()  
                else:
                    os.system('cls||clear')
                    used_letters.append(guess)
                    print(RED + f"Sorry! Letter {guess} in not in the word."+ RESET)
                    print('You loose 1 guess.\n')
                    guesses_remaining -= 1
                    

        else: 
            os.system('cls||clear')
            print(CYAN + 'Congratulations, you won!\n' + 'The gameword is: ' + RESET, gameword)
            break

def display_hangman(guesses_remaining):
    """
    Visual aid to help user follow stages of his progress by displaying animated character 
    """
    stages = [  # final state: head, torso, both arms, and both legs
                MAGENTA +
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """ ,
                # head, torso, both arms, and one leg
                MAGENTA + 
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """
                + RESET,
                # head, torso, and both arms
                MAGENTA +
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """ + RESET ,
                # head, torso, and one arm
                MAGENTA +
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """
                + RESET,
                # head and torso
                MAGENTA + 
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """
                + RESET ,
                # head
                MAGENTA +
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """
                + RESET,
                # initial empty state
                MAGENTA +
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
                + RESET
    ]
    return stages[guesses_remaining]

   







gameword = 'LOVE'
start = intro()
game(gameword)

   

