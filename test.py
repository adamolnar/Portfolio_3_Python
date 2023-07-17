def get_word(word_list):
    """
    Function to pull out guess word for the user from the word_list
    And test it on the test_Word_list to check if words are used random and words 
    Are used from the mocked word_list
    """
    return random.choice(word_list).upper()

test_word_list = ['bad', 'sky', 'capitol', 'fire', 'rain'] 
print(get_word(test_word_list))



def is_word_guessed(gameword, letters_already_guessed):
    """
    Function to compare letters pickes by a user to letters contained in guess word
    If letters in word are equal to letters picked by a user return True and 'do stomething' otherwise return False
    And 'do something'
    """
    if set(gameword) & set(letters_already_guessed) == set(gameword):
        return True
    else:
        return False

test_gameword = 'anna'
test_letters_already_guesses = ["a", 'n']
print(is_word_guessed(test_gameword, test_letters_already_guesses))