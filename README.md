![Screenshot of the game logo](/screenshots/Hangman%20log.png)
## Is there a better way to learn new words if not by plying game and having fun...

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

## Features

### Existing Features

**START**

![Screenshot game start site](/screenshots/Screenshot_game_start.png)

- Game logo printed in color.
- Welcome text to the Hangman Game.
- Two options available to the user. 
- By pressing (1) user is taken directly to the main game page where he can start guessing gameword.
- By pressing (2) user is taken to the Game Rules, where in details is explained how to play this game. Here are also two options available to the user: either they continue to the main game or can exit game.

![Screenshot rules](/screenshots/Screenshot_game_rules%20(1).png)

**MAIN GAME**

![Screenshot main game](/screenshots/Screenshot_main_game.png)

- Firstly the randon word from words.py file is generated.
- User can see how many letters contains game word.
- Each letter is equivalent to one `_` .
- Word definition is added with value from the dictionarys key word, to give to the user a bit of advantage. 
- Computer displays how many guesses are available to the user and how many warnings are left, which are updated after each choice. 
- Available letters are shown in alphabetic order and each time user choses his letter this letter is replaced with red x.
- The visualization of gallows is displayed which is empty. But by each incorrect choice the hangmans body parts are added. 
- Bellow user is asked to enter his choice of the letter.

![Screenshot after first choice](/screenshots/Screenshot_first_choice.png)

- At the top of the terminal A feedback is displayed for the user. If it is incorrect quess, feedback is displayed in red color. If guess is correct feedback is diplayed in yellow color.
- After each letter choice user gets an update on how many moves are left and how many warnings are left. 
- The letter which was picked is replaced in alphabet with the red x.

![Screenshot after correct choice](/screenshots/Screenshot_yellow_feedback.png)

**TYPE YOUR GUESS WORD**

![Screenshot type your guess word](/screenshots/Screenshot_type_your_guess_word.png)

- After user runs out of ramaining guesses, he has a chance to type his guess word and see if it is a match with the game word.
- If the user's guess word match the game word, logo of the game is displayed together with Congratulations feedback.
- The gameword is displayed.
- Finally user is asked if he wants to continue to play or would like to exit the game.

![Screenshot congaratulations](/screenshots/Screenshot_congrats.png)






