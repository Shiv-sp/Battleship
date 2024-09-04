'''
Title: ICS3U Culminating
Description: Covering various coding and python concepts to create a version of Battleship. 
Created By: Shiv Patel
Date Created: 02/06/2022
Date Last Modified: 22/06/2022
'''
# Imports
import shiv

# Bool value to run game
gameStart = False

# Calling of functions to run game
while gameStart == False: 
    gameStart = shiv.menu()

    if gameStart == True:
            userName = shiv.gameIntro () 
            shiv.printBoard (shiv.userBoard, "your")

            userShips = shiv.userBoat (1) 

            shiv.shipPreview (userShips) 

            compRows = shiv.randomRow (shiv.mainBoard) 
            compCols = shiv.randomCol (shiv.mainBoard)

            compBoats = shiv.compShips (compRows, compCols)
            score = shiv.gameRun (shiv.mainBoard, shiv.compBoard, compBoats, userShips.values(), False)
            shiv.results (userName, score)

gameStart = False
