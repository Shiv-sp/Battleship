'''
Title: ICS3U Culminating
Description: Functions File
Created By: Shiv Patel
Date Created: 04/06/2022
Date Last Modified: 22/06/2022
'''
# Imports
from random import randint
from time import sleep 
import os, sys

# Special Function - To play game with minimal time required
def teacher (): 
    typewrite ("Is this Ms. Fisher playing?: \n")

    typewrite ("\na) Yes\n")
    typewrite ("\nb) No\n")

    name = input("\nEnter choice: ")
    clear (0.1)

    if name.lower () == "a":
        typewrite ("Hi Ms. Fisher!\n")
        typewrite ("\nSo BattleShip can be a long & maybe boring game since it's Human vs AI, so I programmed it to be marking friendlier for you if you would like it :)\n")
        typewrite ("\nWhat I mean is that instead of having to guess back and forth vs the AI, I could have it so all 3 outcomes (win, loss, draw) are played out and minimal time is required (co-ordinates are given)\n\n")

        sleep (5)

        typewrite ("Would you like it to be marking-friendly?\n")

        typewrite ("\na) Yes\n")
        typewrite ("\nb) No\n")

        choice = input ("\nEnter Choice: ")

        if choice.lower () == "a":
            typewrite ("\nUnderstood 👍")
            clear (1)
            return True
        else: 
            typewrite ("Understood 👍")
            clear (1)

            return False

    if name.lower () == "b":
        typewrite ("\nIgnore the previous question 😭")
        clear (1)

        return False

# Special Function - Part 2

def teacherMark (): 
    typewrite ("Which option would you like to see?\n")
    typewrite ("\na) User Win\n")
    typewrite ("\nb) CPU Win\n")
    typewrite ("\nc) Draw\n")

    sceneChoice = input("\nEnter Choice: ")

    if sceneChoice.lower () == "a": 
        clear (1)  
        return "a"
    if sceneChoice.lower () == "b":
        clear (1)  
        return "b"
    if sceneChoice.lower () == "c":   
        clear (1)  
        return "c"

def userWin (listA): 
    print ("Here are the CPU ship co-ordinates (Please make a note of them):")
    print ("-----------------------------------")
    for x in listA: 
        print (x) 
    input("\nTo continue please press 'enter':\n>>> ")
    clear (0.1)

# Function to clear console
def clear (time): 
    sleep(time)
    os.system('clear')

# Function to animate text (Inspired by 'Learn Learn Scratch Tutorials' on YouTube)
def typewrite (message):
    for char in message: 
        sys.stdout.write (char)
        sys.stdout.flush()
        sleep (0.1)

# Function to intro game
def gameIntro (): 
    userName = input ("Please Enter Your Name: ")
    clear (0.1)
    typewrite ("Before we start, enjoy this :D\n\n")

    sleep (2)

    typewrite ("               __/___\n")
    typewrite("         _____/______|\n")
    typewrite ("_______/_____\_______\_____\n")
    typewrite ("\              < < <       |\n")
    typewrite ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    print ("\n\n")
  
    typewrite ("Now, let's play Battleship!\n")

    print ("\n\n")

    input("\nTo continue please press 'enter':\n>>> ")
    clear (0.1)

    return userName

# Function to display menu/start game
def menu(): 
    print ("__ )     \  __ __| __ __|  |      ____|   ___|   |   | _ _|   _ \\")  
    print ("__ \    _ \    |      |    |      __|   \___ \   |   |   |   |   |") 
    print ("|   |  ___ \   |      |    |      |           |  ___ |   |   ___/")  
    print ("____/ _/   _\ _|     _|    _____| _____| _____/ _|  _| ___| _|") 

    print ("\n")
    typewrite ("a) Start Game 🕹")
    typewrite ("\nb) Instructions 📖")
    typewrite ("\nc) Recent Results 📊")
    typewrite ("\nd) Exit Game 👋")

    userChoice = input("\n\nPlease choose an option: ")

    clear (0.5)

    if userChoice.lower () == "a":
        clear (0.1)
        start = True
    if userChoice.lower () == "b":
        instructions ()
        start = False
    if userChoice.lower () == "c":
        readScore ()
        start = False
    if userChoice.lower () == "d":
        sys.exit("Please restart if you would like to play again!")
        start = False
    return start 

# Function to display instructions 
def instructions (): 
    print ('''
-> INSTRUCTIONS 
---------------
- The user is tasked to pick 4 locations for their ships to be set on 
- The computer then generates its 4 locations for their ships
- The user & computer guess each others ships location
- If the location is correct, the computer ship is sunken 
- B = Your Boat (You set)
- H = Hit 
- M = Miss
- The first person to lose all 4 ships LOSES!
- ENJOY!
            ''')
    input("\nTo continue please press 'enter':\n>>> ")
    clear (0.1)

# Main battlefield 'board'
mainBoard = []
for grid in range (6): 
    mainBoard.append (["⛴"] * 6)

# Computer 'board'
compBoard = []
for comp in range (6): 
    compBoard.append (["⛴"] * 6)

# User 'board'
userBoard = []
for temp in range (6):
    userBoard.append (["⛴"] * 6)

# Function to print grid
def printBoard (board, text):
    print ("\nHere is", text, "battlefield:")
    print ("------------------------\n")
    column = 1
    print("  ", *range(1,7))
    print (" ")
    for row in board:
        print (column, end = "  ")
        print((" ").join(row))
        column += 1
    print ("\n--------------")

# Function to print 4 random ROW co-ordinates for CPU ships
def randomRow (board): 
    compRow1 = randint (1, (len(board)))
    compRow2 = randint (1, (len(board)))
    compRow3 = randint (1, (len(board)))
    compRow4 = randint (1, (len(board)))
    rowList = [compRow1, compRow2, compRow3, compRow4]
    return rowList

# Function to create 4 random COLUMN co-ordinates for CPU ships
def randomCol (board): 
    compCol1 = randint (1, (len(board)))
    compCol2 = randint (1, (len(board)))
    compCol3 = randint (1, (len(board)))
    compCol4 = randint (1, (len(board)))
    colList = [compCol1, compCol2, compCol3, compCol4]
    return colList 

# Function to create 2D array of all CPU ship locations
def compShips (row, column): 
    location = []

    for i in range (len(row)):
        if [row [i], column [i]] in location: 
            location.append ([randint (1, 6), randint (1,6)])
        else: 
            location.append ([row [i], column [i]])


    return (location)

# Function to ask user for their boat co-ordinates 
def userBoat (boatCount): 
    count = 0
    newBoats = []
    boat = boatCount

    for ship in range (4):
        print ("Boat:", boat)
        row = int(input("\nPlease enter a row co-ordinate for your boat (Co-ordinate from 1-6): "))
        column = int(input("\nPlease enter a column co-ordinate for your boat (Co-ordinate from 1-6): "))
        
        boat +=  1
        clear (1)

        if row < 1 or row > 9 or column < 1 or column > 9:
            print ("Boat:", (boat - 1))
            row = int(input("\nPlease enter a VALID row co-ordinate for your boat (Co-ordinate from 1-6): "))
            column = int(input("\nPlease enter a VALID column co-ordinate for your boat (Co-ordinate from 1-6): ")) 
            clear (1)
        
        else: 
            if ([row, column]) in newBoats: 
                row = int(input("\nPlease enter a new row co-ordinate for your boat (Co-ordinate from 1-6): "))
                column = int(input("\nPlease enter a new column co-ordinate for your boat (Co-ordinate from 1-6): "))
            
                clear (1)
            
        newBoats.append ([row, column])
        gridPreview (userBoard, newBoats, count)
        count += 1
    
    clear (1)

    shipLocation = {"Boat 1":(), "Boat 2":(), "Boat 3":(), "Boat 4":()}

    for i in range (1,5): 
        shipLocation ["Boat "+(str(i))] = newBoats [i-1]
    
    return shipLocation

# Function to preview all user ship co-ordinates
def shipPreview (ships): 
    typewrite ("Here are the co-ordinates for your 4 ships:\n")
    print ("--------------------------------------------")
    
    for key, value in ships.items():
        print(key, ":", value)
    
    print ("\n")
    
    printBoard (userBoard, "your set")

    input("\nTo continue please press 'enter':\n>>> ")
    clear (0.1)

# Function to show the user a preview of their grids
def gridPreview (board, boat, y): 
    x = y
    row = boat [x] [0]
    column = boat [x] [1]

    board [column-1] [row-1] = "B"
    printBoard (board, "your")

# Function to guess co-ordinates
def compGuess (board):
    guess = []
    aiRow = randint (1, (len(board)))
    aiCol = randint (1, (len(board)))
    guess.append ([aiRow, aiCol])

    return guess
 
# Function to run game (both User & CPU)
def gameRun (uBoard, cBoard, cShips, ships, value):
    # Counters
    userTurn = 0
    compTurn = 0
    uBoat = 4
    cBoat = 4
    counter = 0

    run = True

    guessDict = {}
    
    while 1==1:
        # User turn run
        print ("It's your turn! \n\n")
        clear (1)
        
        guessPrint (guessDict)

        print ("\nCPU Ships Remaining:", cBoat)
        userTurn += 1
        print ("\nTurn Number:", userTurn, "\n")

        printBoard (compBoard, "the CPU's")

        print ("\n")
        rowGuess = int(input("Please guess a ROW co-ordinate to strike (From 1-6): "))
        print ("\n")
        print ("\n")
        colGuess = int(input("Please guess a COLUMN co-ordinate to strike (From 1-6): "))

        clear (3)

        if [rowGuess, colGuess] in cShips: # If ship is hit
            cBoat -= 1
            typewrite ("You've sunk a ship of theirs!💣🚢\n")
            print ("\nShip Location Sunk:", [rowGuess, colGuess], "\n")

            cBoard [colGuess-1] [rowGuess-1]  = "H"

            printBoard (compBoard, "the CPU's updated")

            input("\nTo continue please press 'enter':\n>>> ")
            clear (0.1)
        
        else: 
            typewrite ("You missed!\n")
            print ("Your guess was:", [rowGuess, colGuess])
            cBoard [colGuess-1] [rowGuess-1] = "M"
            printBoard (compBoard, "the CPU's updated")
        
       
            input("\nTo continue please press 'enter':\n>>> ")
            clear (0.1)
        
        guessDict ["Guess "+str(userTurn)] = [rowGuess, colGuess]
    
        sleep (1)
        typewrite ("Now it's the CPU's turn!\n")

        # Game 'stats' breakdown
        print ("\nYour Ships Remaining:", uBoat)
        compTurn += 1
        sleep (1.25)
        print ("\nTurn Number:", compTurn)
        sleep (1.25)
        printBoard (mainBoard, "your")

        if value == True: # If special case is selected
            special = marking (ships)
            typewrite ("\nThe CPU guesses ROW: "+ str(special[counter] [0]))
            print ("\n")
            sleep (1.25)
            typewrite ("\nThe CPU guesses COLUMN: "+ str(special [counter] [1]))
            sleep (1.25)

            cGuess = [special [counter][0], special [counter][1]]

            if cGuess in ships: 
                uBoat -= 1
                clear (2)
                typewrite ("The CPU has sunk your ship!")
                print ("\n")
                sleep (1.25)
                print ("Ship Location Sunk:", cGuess)

                uBoard [special [counter][1]- 1] [special [counter][0]-1] = "H"
                print ("\n")
                printBoard (mainBoard, "your updated")

                input("\nTo continue please press 'enter':\n>>> ")
                clear (0.1)

            else: 
                clear (1)
                typewrite ("The CPU missed!")
                print ("\n")
                sleep (1.25)
                print ("It's guess was:", cGuess)
                print ("\n")
                uBoard [special [counter][1]-1] [special [counter][0]-1] = "M"
                sleep (1.25)
                printBoard (mainBoard, "your updated")
                input("\nTo continue please press 'enter':\n>>> ")
                clear (0.1)
            
            counter += 1

        # CPU turn
        else: 
            guess = compGuess (mainBoard)
    
            typewrite ("\nThe CPU guesses ROW: "+ str(guess [0] [0]))
            print ("\n")
            sleep (1.25)
            typewrite ("\nThe CPU guesses COLUMN: "+ str(guess [0] [1]))
            print ("\n")
            sleep (1.25)

            cGuess = [guess [0][0], guess [0][1]]

            if cGuess in ships: 
                uBoat -= 1
            
                print ("\n")
                typewrite ("The CPU has sunk your ship!")
                print ("\n")
                sleep (1.25)
                print ("Ship Location Sunk:", cGuess)

                uBoard [guess [0][1]- 1] [guess [0][0]-1] = "H"
                
                clear (2)
                printBoard (mainBoard, "your updated")

                input("\nTo continue please press 'enter':\n>>> ")
                clear (0.1)

            else: 
                clear (1)
                typewrite ("The CPU missed!")
                print ("\n")
                sleep (1.25)
                print ("It's guess was:", cGuess)
                print ("\n")
                uBoard [guess [0][1]-1] [guess [0][0]-1] = "M"
                sleep (1.25)
                printBoard (mainBoard, "your updated")
                input("\nTo continue please press 'enter':\n>>> ")
                clear (0.1)

        # Final Outcomes (Win/Loss/Draw)
        if uBoat == 0 and cBoat == 0: 
            typewrite ("OH! A DRAW.... HEY AT LEAST YOU DIDN'T LOSE!")
            return "draw"
        
        else:         
            if uBoat == 0: 
                typewrite ("Unfortunatley, The CPU has sunk all your ships before you could sink theirs!\n")
                input("\n\nTo continue please press 'enter':\n>>> ")
                clear (0.1)
                return "CPU"
            if cBoat == 0: 
                typewrite ("CONGRATULATIONS! You have won the game!")
                typewrite ("\nYou sunk all of their ships in "+ str(userTurn)+ " attempts!")
                typewrite ("\nEnjoy this again!\n")
                typewrite ("               __/___\n")
                typewrite("         _____/______|\n")
                typewrite ("_______/_____\_______\_____\n")
                typewrite ("\              < < <       |\n")
                typewrite ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                sleep (3)
                clear (0.1)
                return "user"

# Function to print out dictionary of guesses
def guessPrint (uDict):
    typewrite ("Here are your guesses so far:\n")
    print ("------------------------------------")
    
    for key, value in uDict.items():
        print(key, ":", value)
    print ("------------------------------------")
    print ("\n")
    
# Function to output results into a .txt file
def results (userName, decide): 
    statFile = open("results.txt","r")       

    if decide == "user":
        oldResult = (userName +" VS"+" CPU: ----- WINNER: "+userName+" 🏆"+"\n")
    
    if decide == "CPU":
        oldResult =  (userName +" VS"+" CPU: ----- WINNER: "+"CPU"+" 💻"+"\n")

    if decide == "draw": 
        oldResult = (userName +" VS"+" CPU: ----- DRAW 🤝"+"\n")

    newResult = statFile.readlines()
    newResult.insert(2, oldResult)
    statFile.close()

    statFile = open ("results.txt","w") 
    statFile.writelines(newResult) 
    statFile.close()

# Function to display recent scores (menu option)
def readScore (): 
    inFile = open ("results.txt", "r")
    for i in range (7): 
        print (inFile.readline().strip())
    input("\nTo continue please press 'enter':\n>>> ")
    clear (0.1)

# Special Function - Part 3
def marking (uShips):
    listA = []
    for x in uShips:
        listA.append (x)
    return listA
