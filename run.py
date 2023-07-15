import random
import string 



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
            load_words()
        elif (user_choice1 == '2'):
            print("\n")
            print("RULES")
            print("-> You have to guess the secret word before the stick figure is hung.")
            print("-> The computer will indicate how many letters is in the word. One letter ='_'.")
            print("-> You have six chances to guess the word.")
            print("-> If you choose the letter, that letter will be delited from the list. ")
            print("-> You have 3 warnings: you lose one warning each time 1if you chose a letter which has been already used or symbols which are not letters  ")
            print("\n")
            print("Are you ready now to begin the game?")
            print("(1)Yes, take me to the game.\n(2)No, exit the game.")
            wrong_choice()  
        else:
            print("Wrong choice, please enter your number again.")
        intro()

def wrong_choice(): 
    """
    Function to loop over user choice until he choses correct number to either start the game or exit the game
    """
    user_choice2 = input("-> ")
    for num in user_choice2:
        if (user_choice2 == '1'):
            load_words()
        elif (user_choice2 == '2'):
            print('THE END')
            exit()
        else:
            print("Wrong choice, please enter your number again.")
        wrong_choice()
            
#def load_words():

    

              



start = intro()
print(start)
   

