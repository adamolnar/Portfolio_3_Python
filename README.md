![Screenshot of the game logo](/screenshots/Hangman%20log.png)
## Is there a better way to learn new words if not by plying game and having fun...?

**HANGMAN** is an old school favorite, a word game where the goal is simply to find the missing word. This way of expanding your vocabulary is fun and effective. 

You will be presented with a number of blank spaces representing the missing letters you need to find and deffinition of that word/adjective to give you a little bit of advantage.
Use the keyboard to guess a letter (I recommend starting with vowels).
If your chosen letter exists in the answer, then all places in the answer where that letter appear will be revealed.
After you've revealed several letters, you may be able to guess what the answer is and fill in the remaining letters.
Be warned, every time you guess a letter wrong you loose a life and the hangman begins to appear, piece by piece.

Solve the puzzle before the hangman dies.

[Here is live version of my project.](https://hangman-game-portfolio3-04c41eba22eb.herokuapp.com/)

![Screenshot_am_i_resposive](/screenshots/Screenshot_am_i_resposive.png)

## How to play

- You have to guess the secret word(adjective) before the stick figure is hung.
- The computer will indicate how many letters is in the word.
- You will get a HINT, a word description.
- One letter = '_'.
- You have six chances to guess the word.
- If you choose the letter, that letter will be deleted from the list.
- You have 3 warnings: you lose one warning each time if you chose a letter which has been already used.

## Mock-up:

![Mock-up](/screenshots/Mock_up.png)

## Features/Testing

**START**

![Screenshot game start site](/screenshots/Screenshot_game_start.png)

- Game logo printed in color.
- Welcome text to the Hangman Game.
- Two options available to the user. 
- By pressing (1) user is taken directly to the main game page where he can start guessing gameword.
- By pressing (2) user is taken to the Game Rules, where in details is explained how to play this game. Here are also two options available to the user: either they continue to the main game or can exit game.

![Screenshot rules](/screenshots/Screenshot_rules.png)

**MAIN GAME**

![Screenshot main game](/screenshots/Screenshot_main.png)

- Firstly the randon word from words.py file is generated.
- User can see how many letters contains game word.
- Each letter is equivalent to one `_` .
- Word definition is added with value from the dictionarys key word, to give to the user a bit of advantage. 
- Computer displays how many guesses are available to the user and how many warnings are left, which are updated after each choice. 
- Available letters are shown in alphabetic order and each time user choses his letter this letter is replaced with red x.
- The visualization of gallows is displayed which is empty. But by each incorrect choice the hangmans body parts are added. 
- Bellow user is asked to enter his choice of the letter.

![Screenshot after first choice](/screenshots/Screenshot_false%20.png)

- At the top of the terminal A feedback is displayed for the user. If it is incorrect quess, feedback is displayed in red color. If guess is correct feedback is diplayed in yellow color.
- After each letter choice user gets an update on how many moves are left and how many warnings are left. 
- The letter which was picked is replaced in alphabet with the red x.

![Screenshot after correct choice](/screenshots/Screenshot_correct.png)

**TYPE YOUR GUESS WORD**

![Screenshot type your guess word](/screenshots/Screenshot_type_your_word.png)

- After user runs out of ramaining guesses, he has a chance to type his guess word and see if it is a match with the game word.
- If the user's guess word match the game word, logo of the game is displayed together with Congratulations feedback.
- The gameword is displayed.
- Finally user is asked if he wants to continue to play or would like to exit the game.

![Screenshot congaratulations](/screenshots/Screenshot_congatrs.png)

- If the user's guess word in not a match with gameword, feedback is dispayed in red.
- Finally user is asked if he wants to continue to play or would like to exit the game.

![Screenshot not a match](/screenshots/Screenshot_not_a_mtch.png)


**INPUT VALIDATION AND ERROR-CHECKING**

- If user's choice is invalid, error will be displayed.

![Screenshot of incorrect number entry](/screenshots/Screenshot_error.png)

- If user's choice is invalid, error will be displayed.

![Screenshot of invalid choice](/screenshots/Screenshot_error2.png)

- If the  letter entry is not equal one, error will be displayed.

![Screenshot of invalid multiple letters](/screenshots/Screenshot_oops.png)

- If the user presses wrong key which is not a letter, error will be displayed.

![TEST_1](/screenshots/TEST_1.png)

- Checking for get_word function if it gets random word 

![TEST_2](/screenshots/TEST_2.png)

- Checking for is_word_guessed function to return True if letters guessed are in the gameword or False if it doesn't 

![TEST_4](/screenshots/TEST_4.png)

- Generating underscores equivalent to length of the gameword and placing letter guessed in correct position.


![TEST_5](/screenshots/TEST_5.png)

- Checking if function removes letters already picked from the alphabet. 

![PEP 8](/screenshots/PEP_8.png)

- Passed the code through a PEP8 linter and confirmed there are no problems.
- Given invalid inputs like numbers which are expected, empty input, string instead of letters, same input twice.
- Tested in my local terminal and the Code Institute Heroku terminal.

### Future Features 
- Create larger dictionary to generate new words.
- Create different dicitonaries to allow user to choose the group of word like: animals, countries, movies, famous people etc.
- Create animation for the hangman.
- Create separate button for the clue or word description.


## Bugs

### Solved Bugs 

- AFter user choices guesses ramaining were decreasing accordingly but even when the letter guesses was right, the hangman animaton was showing each part of body being added although my game visialization was to skip the body part added to hangman each time the guessed letter is corect. i Had to add extra variable to store incorrect quesses in order to fix it.

incorrect_guess = 0

- In function game(gameword) after testing guesses remaining were going to -1 although user has only 6 guesses available. I had to change the order of this function which fixed the problem and change value of variable to less than 1.


      elif guesses_remaining == 0:
        os.system('cls||clear')
        print(RED + 'Sorry,no more guesses available.' + RESET)
        print(show_word_underscore(gameword, used_letters))
        print('\n')
        try_to_match()
        print('\n')
        play_again()
      else:
        used_letters.append(guess)
        os.system('cls||clear')
        print(RED + "Sorry!" + RESET)
        print(RED + f"{guess} is not in the word." + RESET)
        print(RED + 'You loose 1 guess.\n' + RESET)
        guesses_remaining -= 1
        incorrect_guess -= 1

      else:
          used_letters.append(guess)
          os.system('cls||clear')
          print(RED + "Sorry!" + RESET)
          print(RED + f"{guess} is not in the word." + RESET)
          print(RED + 'You loose 1 guess.\n' + RESET)
          guesses_remaining -= 1
          incorrect_guess -= 1
          if guesses_remaining < 1:
              os.system('cls||clear')
              print(RED + 'Sorry,no more guesses available.' + RESET)
              print(show_word_underscore(gameword, used_letters))
              print('\n')
              try_to_match()
              print('\n')
              play_again()

- After user runs out of guesses has a choice of either play again the game or exit. When I looped back to function play_again(), gameword was the same as the previous one. I had to wrap up whole game in function run_simulation() in order to generate each tile new word.

- After using colored library for better user experience I have noticed once I set the color for one paragraph it was coloring rest of the text as well. I needed to add RESET at the end of each paragraph in order to keep different text in different colores.



### Remaining Bugs
- No bugs remaining.

### Validator Testing
- PEP 8
  - White spaces
  - To long strings 
  - After all corections no error were returned PEP8online.com

# Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

- Steps for deplyment:
  - After creating an account and logging in, click "New"  
    to create a new app from the dashboard.
  - Create a new Heroku app.
  - Create a unique name for the app and select my region; press "Create app".
  - Go to "Settings" and navigate to Config Vars.
  - Add Config Vars.
    - For this app was used: KEY = PORT : VALUE = 8000.
  - Set the buildbacks to Python and NodeJS in that order.
  - Link the Heroku app to the repository.
  - Click on **Deploy**.

# Credits

- Code Institute for the deployment terminal.
- Code Institute Project Scope [Code Institute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/).
- Hangman animation from [GitHubGist](https://gist.github.com/lupinetti/8f89e5f33750aa7c91c3).
- Hangman Tutorial: [How to build HANGMAN with Python in 10 MINUTES](https://www.youtube.com/watch?v=m4nEnsavl6w).
- How to build alphabet range in Python from [StackOverflow](https://stackoverflow.com/questions/16060899/alphabet-range-in-python).
- How to use random library [Random-Word 1.0.11](https://pypi.org/project/Random-Word/).
- How to use colored library [colored 2.2.3](https://pypi.org/project/colored/).
- How to Print Colored Text in Python [StudyTonight](https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python#:~:text=We%20can%20use%20the%20built,and%20get%20your%20desired%20output.).
- How can I get a random key-value pair from a dictionary [StackOverflow](https://stackoverflow.com/questions/4859292/how-can-i-get-a-random-key-value-pair-from-a-dictionary).
- Inspiration from [HangmanGame](https://thewordsearch.com/hangman/).
- Dictionary [Lingoda](https://blog.lingoda.com/en/top-50-adjectives-in-english-you-need-to-know/).














