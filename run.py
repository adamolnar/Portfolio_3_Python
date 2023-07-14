import random
import string 




print("Welcome to the Hangman Game!")
print("Do you know the rules")
print("(1)Yes, take me to the game.\n(2)No, show me the rules")

user_choice = input("->")
print(user_choice)

def load_words():
    """
    This function gets words from the library and inserts them in one virable
    """
    word_list =  open('words.txt', 'r').readline().split
    return word_list

def random_word(word_list):
    """
    Function to get random word from the word_list
    Return random word and test it 
    """
    return random.choice(word_list)

test_word_list = ['sun', 'sky', 'water', 'fire', 'nature'] 
print(random_word(test_word_list))


