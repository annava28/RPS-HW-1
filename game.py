
# customizing player name
import os 
player_name = os.getenv("PLAYER_NAME", default="Player One")

# welcoming the user
print("---------------------------------------------------------------")
print("Welcome", player_name, "to an intense game of Rock, Paper, Scissors. Hope you're ready...")
print("---------------------------------------------------------------")

# ask for user input
user_weapon = input("Please select your weapon: 'Rock', 'Paper', 'Scissors': ")
print("---------------------------------------------------------------")
# validations
acceptable = "Rock rock ROCK paper Paper PAPER Scissors scissors SCISSORS"

if user_weapon not in acceptable:
    print ("Oh no! Please ensure you have selected correctly from the above weapons.")
    quit()
else: 
    print(player_name, "chose:", user_weapon)
    
# computer choice

import random
options = ["rock", "paper", "scissors"]

ai_weapon = random.choice(options)

print("The SUPER intelligent AI chose:", ai_weapon)
print("---------------------------------------------------------------")

# determine the winner + displaying result 
# adapted from Marie-Eugenie Chandon-Moet on Slack

if user_weapon == ai_weapon:
    print("Both players played", user_weapon, "An even match!")
elif user_weapon == "paper":
    if ai_weapon == "rock":
        print("Paper covers rock. You won!")
    else:
        print("Scissors cuts paper. You lost. Better luck next time!")
elif user_weapon == "scissors":
    if ai_weapon == "paper":
        print("Scissors cuts paper. You won!")
    else:
        print("Rock crushes scissors. You lost. Better luck next time!")
elif user_weapon == "rock":
    if ai_weapon == "scissors":
        print("Rock crushes scissors. You won!")
    else:
        print("Paper covers rock. You lost. Better luck next time!")

# goodbye message
print("---------------------------------------------------------------")
print("Wow! Wasn't that riveting? Hope you're ready for another round...")
