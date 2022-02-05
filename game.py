


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#





# ask for user input

weapon = input("Please select your weapon: 'Rock', 'Paper', 'Scissors': ")

# validations

acceptable = "Rock rock ROCK paper Paper PAPER Scissors scissors SCISSORS"

if weapon not in acceptable:
    print ("Ensure you have selected correctly from the above choices")
else: 
    print("You chose: ", weapon)
    


# computer choice

import random
options = ["rock", "paper", "scissors"]

ai_choice = random.choice(options)

print("Super intelligent AI chose: ", ai_choice)


# determine the winner




# display the final result


