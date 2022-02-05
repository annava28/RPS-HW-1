
# welcoming the user
print("Welcome 'Player One' a riveting game of Rock, Paper, Scissors. Hope you're ready.")

# ask for user input
user_weapon = input("Please select your weapon: 'Rock', 'Paper', 'Scissors': ")

# validations

acceptable = "Rock rock ROCK paper Paper PAPER Scissors scissors SCISSORS"

if user_weapon not in acceptable:
    print ("Please ensure you have selected correctly from the above weapons.")
    quit()
else: 
    print("You chose: ", user_weapon)
    

# computer choice


import random
options = ["rock", "paper", "scissors"]

ai_weapon = random.choice(options)

print("The super intelligent AI chose: ", ai_weapon)


# determine the winner
# adapted from Marie-Eugenie Chandon-Moet on Slack

if user_weapon == ai_weapon:
    print("You both wielded ", user_weapon, ". A worthy match - it's a tie!"
elif user_weapon == "paper":
    if ai_weapon == "rock":
        print("Paper suffocates rock. You won the battle!")
    else:
        print("Scissors viciously cuts paper. You lost the battle. Better luck next time!")
elif user_weapon == "scissors":
    if ai_weapon == "paper":
        print("Scissors viciously cuts paper. You won the battle!")
    else:
        print("Rock obliterates scissors. You lost the battle. Better luck next time!")
elif user_weapon == "rock":
    if ai_weapon == "scissors":
        print("Rock obliterates scissors. You won!")
    else:
        print("Paper suffocates rock You lost! It’s ok.")

# display the final result


