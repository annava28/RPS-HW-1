
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
#https://www.w3schools.com/python/ref_string_capitalize.asp

acceptable = "Rock rock ROCK paper Paper PAPER Scissors scissors SCISSORS"

if user_weapon not in acceptable:
    print ("Oh no! Please ensure you have selected correctly from the above weapons.")
    quit()
else: 
    user_weapon = user_weapon.capitalize() #standardization of inputs for validation
    print(player_name, "chose:", user_weapon)
    
# computer choice

import random
options = ["Rock", "Paper", "Scissors"]

ai_weapon = random.choice(options)

print("The SUPER intelligent AI chose:", ai_weapon)
print("---------------------------------------------------------------")

# determine the winner + displaying result 
# adapted from Marie-Eugenie Chandon-Moet on Slack

if user_weapon == ai_weapon:
    print("Both players played", user_weapon, ". It's a tie!")
elif user_weapon == "Paper":
    if ai_weapon == "Rock":
        print("Paper covers rock. You won!")
    else:
        print("Scissors cuts paper. You lost. Better luck next time!")
elif user_weapon == "Scissors":
    if ai_weapon == "Paper":
        print("Scissors cuts paper. You won!")
    else:
        print("Rock crushes scissors. You lost. Better luck next time!")
elif user_weapon == "Rock":
    if ai_weapon == "Scissors":
        print("Rock crushes scissors. You won!")
    else:
        print("Paper covers rock. You lost. Better luck next time!")
else:
    print("Computer error. Please try re-running the program!")



# goodbye message
print("---------------------------------------------------------------")
print("Wow! Wasn't that riveting? Hope you're ready for another round...")
