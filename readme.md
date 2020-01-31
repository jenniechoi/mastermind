# How to run the code
* Open terminal and navigate to project folder ‘Mastermind’
* Run ‘$python manage.py runserver’
* Open browser to ‘http://localhost:8000/’ to start app
## Document thought process and/or code structure
There are three major components to the game: start, game play, and results.
## Start
* A multiple choice form is called for the user to select the difficulty. Once they select, ‘start_game’ function in the API file will call the random integer generator web API. Based on their selection, the API call will have a parameter for 3, 4, or 5 numbers. The answer has all white spaces removed. A game will be created in the ‘Game’ database to save the difficulty and generated answer. The ‘start_game’ function will end with returning the newly created Game database ID. Then the user is redirected to the game play.
## Game
* Once the game function is called in ‘Views’, it calls the Game database based on the ID from the input. This provides the answer, number of times guessed (guess_count), and the difficulty level selected. If the data shows that the user guessed correctly or has guessed 10 times, the user will be redirected to the ‘Results’ page with the given game_id.
* Otherwise, based on the difficulty level the correct form will be displayed (3, 4, or 5 digits to guess). The user will be told to guess the combination.
* Once a guess is submitted the guess, how many times the user has guessed for the game, and answer are given to the API. In the API, ‘check_guess’ function increase the count for number of guesses, and checks to see if the guess matches the answer. If it does, then the game table is updated to reflect the correct guess was made.
* If the guess is wrong, the guessed digits and indices are saved into a dictionary along with the answer counterparts. If a guess is in the answer, it will be saved into a list. That list is then evaluated to determine how many digits guessed are correct and how many spots are correct.
* The guess is added to the database under a new “Guess” entry. The game is then updated to reflect that another guess has been made. The difficulty is then used to ensure the correct number of digits are in the form. In the ‘Views’, the user is then redirected to either the results page (if the number of guesses is 10 or correct) or the game page to guess again.
## Results
* If the user reaches 10 guesses or has the correct guess, they are redirected to the ‘Results’ page from ‘View’. Using the given game ID, the ‘get_results’ function in the API is called. The function calls the database to look at past game and guess results. From there, the HTML page displays the results. This includes letting the user know if they won/lost, all past game wins results broken out by difficulty, and detailed results from the game the user just played. This includes the answer, difficulty, and all past guesses with the numbers/position that were correctly guessed in the game the user just played.
* If the user chooses to click on the Play Again button, they are redirected back to ‘home’ to select difficulty and start again.

# Extensions
* Store all past guess/game data in database
* Display results for last played game in results page after 10 guesses or correct guess
* Display results for all played games in the database
* Select level of difficulty at the start of the game which will make the user guess 3, 4, or 5 digits
