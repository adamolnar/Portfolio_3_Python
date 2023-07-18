import random
from words import word_list
import string
from colored import fg


print("Welcome to the Hangman Game!")
print("Do you know the rules?")
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
            print("This is where the fun begins!")
            print("\n")
            get_word('word_list')
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
            print("Incorrect number, please enter your choice again.")
        intro()

def wrong_choice(): 
    """
    Function to loop over user choice until he choses correct number to either start the game or exit the game
    """
    user_choice2 = input("-> ")
    for num in user_choice2:
        if (user_choice2 == '1'):
            get_word('word_list')
        elif (user_choice2 == '2'):
            print('THE END')
            exit()
        else:
            print("Incorrect number, please enter your choice again.")
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
            
test_letters_already_guessed = ['B', 'M', 'R', 'T']
color = fg('green')
print(color + available_letters(test_letters_already_guessed))












gameword = get_word()
start = intro()

   

