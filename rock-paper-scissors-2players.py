"""
Classic Rock Paper scissors game
Two players
The game only ends when a player wins
"""
import random
import getpass

def play():
    print("Type s for scissors, r for rock or p for paper: ")
    player_one  = getpass.getpass(prompt = "Player One: ") # Hide player_one's input to make the game fair
    #player_one = input("Player One: ")
    player_one = player_one.lower()
    player_two = input("Player Two: ")
    print("Player One:",player_one)
    player_two = player_two.lower()
    if (player_one == "r" or player_one == "p" or player_one == "s") and (player_two == "r" or player_two == "p" or player_two == "s"):
        if player_two == player_one:
            print("Draw! \nPlay Again...")
            return play()
        if ((player_two == "r" and player_one == "p") or  (player_two == "p" and player_one == "s") or  (player_two == "s" and player_one == "r")):
            return "Congratulations Player One! You Won.."
        return "Congratulations Player Two! You Won.."
    else:
        print("Invalid input. Follow the instruction")
        return play()

print("WELLCOME TO ROCK PAPER SCISSORS GAME")
print(play())