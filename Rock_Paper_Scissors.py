import random

def getChoices():
    playerChoice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computerChoice = random.choice(options)
    choices = {"player": playerChoice, "computer": computerChoice}
    return choices

def checkWin(player, computer):
    print(f"You chose: {player}, computer chose: {computer}")
    if player == computer:
        return "It's a tie"
    
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose!"
    
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose!"
    
    elif player == "Scissors":
        if computer == "Paper":
            return "Scissors cuts Paper! You win!"
        else:
            return "Rock smashes Scissors! You lose!"

choices = getChoices()    
result = checkWin(choices["player"], choices ["computer"])

print(result)