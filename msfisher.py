'''
Title: ICS3U Culminating
Description: Same game, but an 'alt' file for Ms.Fisher (marking-friendly)
Created By: Shiv Patel
Date Created: 02/06/2022
Date Last Modified: 22/06/2022
'''
# Imports
import shiv

# Bool value to run game
gameStart = False

# Calling of functions to run game (Modifed Version)
while gameStart == False:
     
    gameStart = shiv.menu()

    if gameStart == True:
        markingEasier = shiv.teacher()

        if markingEasier == True: 
            scenario = shiv.teacherMark()

            if scenario == "a":
                print ("Scenario 1: USER WINS\n")
                shiv.clear (2)
                userName = shiv.gameIntro () 
                shiv.printBoard (shiv.userBoard, "your")

                userShips = shiv.userBoat (1) 

                shiv.shipPreview (userShips) 

                compRows = shiv.randomRow (shiv.mainBoard) 
                compCols = shiv.randomCol (shiv.mainBoard)

                compBoats = shiv.compShips (compRows, compCols)
                shiv.userWin (compBoats) # Special Function to help complete game
                score = shiv.gameRun (shiv.mainBoard, shiv.compBoard, compBoats, userShips.values(), False)
                shiv.results (userName, score)
                shiv.clear (0.1)
                shiv.os.execl(shiv.sys.executable, shiv.sys.executable, *shiv.sys.argv) # Adapted from StackOverflow (Restart Games after execution of each scenario)

            if scenario == "b":
                print ("Scenario 2: CPU WINS\n")
                shiv.clear (2)
                userName = shiv.gameIntro () 
                shiv.printBoard (shiv.userBoard, "your")

                userShips = shiv.userBoat (1) 

                shiv.shipPreview (userShips) 

                compRows = shiv.randomRow (shiv.mainBoard) 
                compCols = shiv.randomCol (shiv.mainBoard)

                compBoats = shiv.compShips (compRows, compCols)
                
                score = shiv.gameRun (shiv.mainBoard, shiv.compBoard, compBoats, userShips.values(), True)
                shiv.results (userName, score)
                shiv.clear (0.1)
                shiv.os.execl(shiv.sys.executable, shiv.sys.executable, *shiv.sys.argv) # Adapted from StackOverflow (Restart Games after execution of each scenario)
                
            if scenario == "c":
                print ("Scenario 3: DRAW/TIE\n")
                print ("\nFor this scenario, it is necessary that you enter each CPU co-ordinate correctly and not mess up any turns or else the Draw will not work.")
                input("\nTo continue please press 'enter':\n>>> ")
                shiv.clear (0.1)
                userName = shiv.gameIntro () 
                shiv.printBoard (shiv.userBoard, "your")

                userShips = shiv.userBoat (1) 

                shiv.shipPreview (userShips) 

                compRows = shiv.randomRow (shiv.mainBoard) 
                compCols = shiv.randomCol (shiv.mainBoard)


                compBoats = shiv.compShips (compRows, compCols)
                shiv.userWin (compBoats) # Special Function to help complete game
                
                score = shiv.gameRun (shiv.mainBoard, shiv.compBoard, compBoats, userShips.values(), True)
                shiv.results (userName, score)
                shiv.clear (0.1)
                shiv.os.execl(shiv.sys.executable, shiv.sys.executable, *shiv.sys.argv) # Adapted from StackOverflow (Restart Games after execution of each scenario)
        
        else: # Regular Game option
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


    