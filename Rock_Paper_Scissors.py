import random

def getChoices():
    playerChoice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computerChoice = random.choice(options)
    choices = {"player": playerChoice, "computer": computerChoice}
    return choices

def checkWin(player, computer):
    return[player, computer]
