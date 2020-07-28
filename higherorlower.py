### AUTHOR: SkipperHQ
### DATE STARTED: 28/07/2020
### PROGRAM NAME: Higher or Lower
### PROGRAM DESCRIPTION: My first real attempt at finishing a Python project I started. Was fun, hoping this is one of many.

import random
import time
import os
import sys

playerTries = 0

class game:
    def __init__(self):
        self.robotChoice = False
        self.playerChoice = False
        
    def main():
        print("Welcome, start a new game?\nSelect an option using the number to the left of the respective option.\n1. New Game\n2. Statistics\n3. Exit Game")
        userInput = input("> ")
        if userInput == "1" or userInput.title() == "New" or userInput.title() == "Start":
            print("Starting Game...")
            global playerTries
            playerTries = 0
            game.gameScreen()
        elif userInput == "2" or userInput.title() == "Stats":
            pass
        elif userInput == "3" or userInput.title() == "Exit" or userInput.title() == "Quit":
            sys.exit()

    def gameScreen():
        self.robotChoice = random.randint(0,100)
        print("Robot: I have selected a number between 1 and 100. Have a guess.")
        game.core(playerTries)
 
    def core(playerTries):
        self.playerChoice = int(input("> "))
        if self.playerChoice < 101:
            if self.playerChoice > 0:
                if self.playerChoice < self.robotChoice:
                    print("Higher")
                    playerTries = playerTries + 1
                    if playerTries == 1:
                        print("This is your first try.")
                        game.core(playerTries)
                    elif playerTries > 1:
                        print("You've had", playerTries, "tries")
                        game.core(playerTries)
                elif self.playerChoice > self.robotChoice:
                    print("Lower")
                    playerTries = playerTries + 1
                    if playerTries == 1:
                        print("This is your first try.")
                        game.core(playerTries)
                    elif playerTries > 1:
                        print("You've had", playerTries, "tries")
                        game.core(playerTries)
                else:
                    game.gameOver()


    def gameOver():
        if self.playerChoice == self.robotChoice:
            print("Robot: You win! Congratulations!")
        else:
            print("Robot: Try Again.")
            game.core()

self = game
game.main() 
