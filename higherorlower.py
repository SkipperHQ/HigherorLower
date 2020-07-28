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
        
    # Start of main menu where you can start the game, soon, there might be functionality for a highscores menu for the client computer.
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
    # Selects the robot's number and sends player to the main game.
    def gameScreen():
        self.robotChoice = random.randint(0,100)
        print("Robot: I have selected a number between 1 and 100. Have a guess.")
        game.core(playerTries)
 
    # Start of main game function
    def core(playerTries):
        self.playerChoice = int(input("> "))
        # Two lines underneith serve to ensure that user doesn't select anything above 100 or lower than 1.
        if self.playerChoice < 101:
            if self.playerChoice > 0:
                # Below are the lines of code that decide whether the two numbers are the same or whether player's code is higher/lower than robots.
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
                    # Sends to gameOver() function
                    game.gameOver(playerTries)

            else:
                print("Number is too low, please select a number between 1 and 100.")
                game.core(playerTries)

        else:
            print("Number is too high, please select a number between 1 and 100.")
            game.core(playerTries)


    def gameOver(playerTries):
        # If the two numbers are the same, you win. The else statement is just there in case of a weird error, just a possibility.
        if self.playerChoice == self.robotChoice:
            print("Robot: You win! Congratulations!\nYou won with", playerTries, "tries!\nPress Enter to Continue...")
            userInput = input("> \n")
            game.main()
            
        else:
            print("Robot: Try Again.")
            game.core()

self = game
game.main() 
