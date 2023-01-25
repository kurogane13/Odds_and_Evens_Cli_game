# Odds_and_Evens_Cli_game

# Python cli numbers game

About the game and scope:

This is a python cli based game, about odd and even numbers. 

- The game is based on arrays, that are created separately, for both odd, and even numbers.
- The user must choose to be either in the odds or even team. 
- Provide an amount of points to reach.
- Set the maximum number, from which the computer will genereate a random number between 0, and this number.
- Once all the above is set, you are ready to start the game. The first team that reaches the amount of points is the winner.

Available modes:

    - Mode 0: Computer automatic mode. The computer plays both players.
    - Mode 1: Manual Mode. You can play by yourself, or with a partner.  
    - Mode 2: Fast mode. The computer plays against itself, at full speed.
  
Aditional features:

  The game records a log of the games played with date and time contained in a file called 'odds_and_evens.log', and it saves it in the path were the game   was executed.  
  
How to run the game?: 

    - Import the following libraries:
      - random
      - time
      - datetime
      - from datetime import datetime
    - Run the game with your python 3 version: python3.x odds_evens_game.py
    
NOTE: There is a folder named Game_Screenshots, were you can preview what the cli game looks like.
