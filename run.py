import random
import string 


def intro():
    """
    Function to determine action after user choice.
    Either user beginnes the game without further informations, or he gets to know the rules.
    If inncorect number is chosen it asks user to repet the action.
    """
    print("Welcome to the Hangman Game!")
    print("Do you know the rules?")
    print("(1)Yes, take me to the game.\n(2)No, show me the rules.")
    user_choice = input("-> ")
        
    if (user_choice == '1'):
        print("This is where the fun begins!")
        load_words()
    elif (user_choice == '2'):
        print("\n")
        print("RULES")
        print("-> You have six chances to guess the word.")
        print("-> If You chose the letter, it will be delited from the list.")
        print("-> You have 3 warnings: you lose one warning if you chose a letter which has been already used or symbols which are not letters  ")  
    else:
        print("Wrong choice, please enter your number again.")
        intro()

                

def load_words():
    """
    This function gets words from the library and inserts them in one variable
    """
    word_list =  open('words.txt', 'r').readline().split
    return word_list

def random_word(word_list):
    """
    Function to get random word from the word_list
    Return random word and test it 
    """
    return random.choice(word_list)

test_word_list = ['hair', 'bug', 'water', 'rain', 'nature'] 
print(random_word(test_word_list))


start = intro()
print(start)
   

