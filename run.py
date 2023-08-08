import random
import string
import pyfiglet
import os
from colored import fg
from words import word_list

"""
Color variables to create user experience friendly colored text
"""
BLACK = '\033[30m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = "\033[1;96m"
UNDERLINE = '\033[4m'
RESET = '\033[0m'


def run_simulation():
    """
    Game logo with use of pyfiglet library
    """
    os.system('cls||clear')
    logo = pyfiglet.figlet_format("Hangman Game", font="digital")
    print(CYAN + logo + RESET)

    print(YELLOW + UNDERLINE + "Welcome to the Hangman Game!" + RESET)
    print("\n")
    print(GREEN + "Do you know the rules?" + RESET)
    print("(1)Yes, take me to the game.\n(2)No, show me the rules.")

    def intro():
        """
        Function to determine action after user choice.
        Either user beginnes the game without further informations
        Or he gets to know the rules.
        If inncorect number is chosen it asks user to repet the action.
        """
        user_choice1 = input("-> ")
        for num in user_choice1:
            if (user_choice1 == '1'):
                print(CYAN + logo + RESET)
                print(YELLOW + "This is where the fun begins!\n" + RESET)
                game(gameword)
            elif (user_choice1 == '2'):
                os.system('cls||clear')
                print(CYAN + logo + RESET)
                print(YELLOW + UNDERLINE + "GAME RULES:" + RESET)
                print("-> You have to guess the secret word(adjective)")
                print("   before the stick figure is hung.")
                print("-> The computer shows how many letters is in the word.")
                print("-> You will get a HINT, a word description.")
                print("-> One letter = '_'.")
                print("-> You have six chances to guess the word.")
                print("-> If you choose the letter,")
                print("   that letter will be deleted.")
                print("-> You have 3 warnings: ")
                print("   you lose one warning each time if ")
                print("   you chose a letter which has been already used.")
                print("\n")
                print(YELLOW + UNDERLINE + "Start the game?" + RESET)
                print("(1)Yes, take me to the game.\n(2)No, exit the game.")
                wrong_choice()
            else:
                print(RED + "Incorrect number, enter choice again." + RESET)
            intro()

    def wrong_choice():
        """
        Function to loop over user choice until he choses
        Correct number to either start the game or exit the game
        """
        user_choice2 = input("-> ")
        for num in user_choice2:
            if (user_choice2 == '1'):
                game(gameword)
            elif (user_choice2 == '2'):
                os.system('cls||clear')
                print(CYAN + logo + RESET)
                print(YELLOW + 'BYE BYE' + RESET)
                print('\n')
                exit()
            else:
                print(RED + "Incorrect number, enter choice again." + RESET)
            wrong_choice()

    def get_word():
        """
        Function to pull out guess word key and value from the dictionary
        """
        key_value = random.choice(list(word_list.items()))
        tuple = list(key_value)
        word = tuple[0]
        value = tuple[1]
        return word, value

    def is_word_guessed(gameword, used_letters):
        """
        Function to compare letters pickes by a user
        To letters contained in guess word
        If letters in word are equal to letters picked by a user
        Return True and 'do stomething' otherwise return False
        and 'do something'
        """
        if set(gameword) & set(used_letters) == set(gameword):
            return True
        else:
            return False

    def show_word_underscore(gameword, used_letters):
        """
        Show to user the gameword by displaying number of '_'
        Equivalent to length of the word
        Allow user to see the number of guessed letters
        And remaining letters that are needed to be guessed.
        """
        result_list = []
        for i in range(len(list(gameword))):
            if list(gameword)[i] in set(used_letters):
                result_list.append(list(gameword)[i])
            else:
                result_list.append("_ ")
        return ' '.join(map(str, result_list))

    def avb_letters(used_letters):
        """
        Function to return alphabet letter
        Without letters which has been picked by the user
        User can see what letters are still available to pick
        To avoid choosing the same letters
        """
        still_available = list(string.ascii_uppercase)

        for i in range(-len(still_available), 0):
            if still_available[i] in used_letters:
                still_available[i] = (RED + "x" + GREEN)
        return ' ' .join(still_available)

    def try_to_match():
        """
        After running ou of guesses user can enter his choice of word and
        See if it matches with the gameword
        """
        print(BLUE + 'HINT FOR YOU: -->', word_value + RESET)
        print('\n')
        print('Please type your guess word?\n')
        try_out = str.upper(input())
        print('\n')
        if set(try_out) == set(gameword):
            os.system('cls||clear')
            print(CYAN + logo + RESET)
            print(CYAN + 'Congratulations! The gameword is:', gameword + RESET)
            print('\n')
            play_again()
        elif len(try_out) == 0:
            os.system('cls||clear')
            print(CYAN + logo + RESET)
            print(RED + 'Error. Please enter your word!' + RESET)
            print('\n')
            pass
        else:
            os.system('cls||clear')
            print(CYAN + logo + RESET)
            print(RED + 'Sorry, not a match. The word is:', gameword + RESET)
            print('\n')
            play_again()
        try_to_match()

    def play_again():
        """
        Choice for the user to play again or to exit game
        """
        print(YELLOW + 'Would you like to play again?\n' + RESET)
        play = input('Y/N \n').upper()
        if play == 'Y':
            os.system('cls||clear')
            run_simulation()
        elif play == 'N':
            os.system('cls||clear')
            print(CYAN + logo + RESET)
            print(YELLOW + 'Bye, bye!\n' + RESET)
            exit()
        else:
            os.system('cls||clear')
            print(CYAN + logo + RESET)
        play_again()

    def game(gameword):
        """
        Function to implement the body of the program and
        Use previouse functions whitin this body
        Determine user choices scenario
        """
        os.system('cls||clear')
        used_letters = []
        guessed = False
        guesses_remaining = 6
        warnings_remaining = 3
        incorrect_guess = 6
        print('The gameword is loading...')
        print('A gameword is', len(gameword), 'letters long.')

        while True:
            """
            Decrease user remaining guesses and warning
            Each time letter is entered by user
            If incorrect sign or repeating previusly picked letter
            Is entered user is not losing guesses or wanrings
            If previously chosen letter is picked again, user looses 1 warning
            """
            if not is_word_guessed(gameword, used_letters):
                print(show_word_underscore(gameword, used_letters))
                print('\n')
                print(BLUE + 'WORD DEFFINITION: -->', word_value + RESET)
                print('You have', int(guesses_remaining), "guess(es) left\n")
                print('and', int(warnings_remaining), 'warning(s) left!', '\n')
                print(GREEN + "Letters:", avb_letters(used_letters) + RESET)
                print(display_hangman(incorrect_guess))
                guess = str.upper(input('Please enter letter of your choice:'))
                print('\n')

                if guessed is False:
                    if not guess.isalpha():  # If key pressed is not a letter
                        os.system('cls||clear')
                        print(RED + 'Oops! Wrong key. Try again!\n' + RESET)
                    elif len(str(guess)) != 1:  # If the key pressed multiple
                        os.system('cls||clear')
                        print(RED + 'Oops! Try again!\n' + RESET)
                    elif guess in used_letters:  # If the letter was used
                        os.system('cls||clear')
                        warnings_remaining -= 1
                        print(RED + 'This letter was already used!\n' + RESET)
                        if warnings_remaining == 0:  # If user out of warning
                            os.system('cls||clear')
                            print(RED + 'You run out of warning!' + RESET)
                            print(RED + f'The word was: {gameword}.' + RESET)
                            print(RED + 'Good luck next time!' + RESET)
                            print('\n')
                            play_again()
                    elif guess in set(gameword):  # If user guess is corect
                        os.system('cls||clear')
                        print(YELLOW + 'You got it right!\n' + RESET)
                        used_letters.append(guess)
                        guesses_remaining -= 1
                    else:  # If user guess is incorrect
                        used_letters.append(guess)
                        os.system('cls||clear')
                        print(RED + "Sorry!" + RESET)
                        print(RED + f"{guess} is not in the word." + RESET)
                        print(RED + 'You loose 1 guess.\n' + RESET)
                        guesses_remaining -= 1
                        incorrect_guess -= 1
                        if guesses_remaining > 1:  # If runs out of 6 guesses
                            os.system('cls||clear')
                            print(RED + 'Sorry,no guesses available.' + RESET)
                            print(show_word_underscore(gameword, used_letters))
                            print('\n')
                            try_to_match()
                            print('\n')
                            play_again()
            else:  # If user guess gameword
                os.system('cls||clear')
                print(CYAN + 'Congratulations!\n' + RESET)
                print(CYAN + f'The gameword is:', gameword + RESET)
                print('\n')
                play_again()
        game(gameword)

    def display_hangman(incorrect_guess):
        """
        Visual aid to help user follow stages of his progress
        By displaying animated character
        Copied from YouTube Tutorial
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
                    """
                    + RESET,
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
                    """ + RESET,
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
                    + RESET,
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
        return stages[incorrect_guess]

    word_items = get_word()
    gameword = word_items[0]
    word_value = word_items[1]
    start = intro()
    game(gameword)
    again = play_again()


run_simulation()
