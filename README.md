## Run instructions
**LINUX or MAC** : To run this program, open up a terminal, navigate to your directory, clone this repo then type `pipenv run python3 main.py`

## Unit testing
`pipenv run pytest test_connect_four.py`
### Improvements
- Create a UI using tkinter for users to interact
- Option for 2 or more players
- AI Engine based on reinforcement learning
- Allow the player to set up the board and game with different rules: Pop out, Pop 10, Five in a row, Power up
- Add custom markers for each player in the player object
- Represent the winning line with a strikeout instead of just double 88s
- Add diagnoal checks for 3s in bot move
- Add in more logic for the bot moves based on the next player's following move
- Add in logic for bot to add a piece where it is not consecutive eg. 2, 2, 0, 2
- Testing more cases for the bot moves. Testing each and every condition in the `get_bot_move` function
