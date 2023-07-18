# TEST 1
def get_word(word_list):
    """
    Function to pull out guess word for the user from the word_list
    And test it on the test_Word_list to check if words are used random and words 
    Are used from the mocked word_list
    """
    return random.choice(word_list).upper()

test_word_list = ['bad', 'sky', 'capitol', 'fire', 'rain'] 
print(get_word(test_word_list))


# TEST 2
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


# TEST 3
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

test_gameword = 'apple'
test_letters_already_guessed = ['p']
print(show_guessed_word(test_gameword, test_letters_already_guessed))

#TEST4 
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
print(available_letters(test_letters_already_guessed))