"""
                        🚀 Frontier Tech Leaders Programme
||||||||||||||||||||||||||||||||| ASSIGNMENT 2 ||||||||||||||||||||||||||||||||||

"""
import os
import asyncio
import random

#This is just an animation to show on the screen that the program is loading... 
async def load(process):
    os.system("clear")
    print(f"{process} is loading.")
    await asyncio.sleep(1)
    os.system("clear")
    print(f"{process} is loading..")
    await asyncio.sleep(1)
    os.system("clear")
    print(f"{process} is loading...")
    await asyncio.sleep(1)
    os.system("clear")


#Draw function
def drawBoard(row:int, column:int,rowT:int, columnT:int,ranXRow=None,ranXColumn=None):
    
    characterAs:str="*"
    characterT:str="T"
    characterX:str="X"

    if not (ranXRow and ranXColumn) or ranXColumn>column or ranXRow>row:
        ranXRow=random.randint(1,row)
        ranXColumn=random.randint(1,column)
    
    print("Here's your game board:\n")
    for n in range(1,row+1):
        for m in range(1,column+1):

            #Place Treasure (T) on the board
            if n ==rowT and m==columnT:
                print(characterT,end=" ")
                continue
            
            #Avoid overlap between X and T
            if(rowT==ranXRow and columnT==ranXColumn):
                ranXRow=random.randint(1,row)
                ranXColumn=random.randint(1,column)

            #Randomly place a trap (X) on the board
            elif(n==ranXRow and m==ranXColumn):
                print(characterX,end=" ")
                continue
            
            #Filling with asterisks (*)
            print(characterAs,end=" ")

        print("")

def play(row:int,column:int,rowT:int,columnT:int):

    drawBoard(row,column,rowT,columnT)

    while True:
       
        print("\n===Guess the location of the treasure===\n")
        x=int(input(f"Choose a row (1-{row}): "))
        y=int(input(f"Choose a column: (1-{column}): "))
        
        if x==rowT and y==columnT:
            return True
        
        drawBoard(row,column,rowT,columnT,x,y)
        print("\nWrong guess! (Try Again...)")
    
    #return False
        


try:
    #loading...
    asyncio.run(load("Program"))

    row=int(input("Enter the number of rows for the game board: "))
    column=int(input("Enter the number of columns for the game board: "))

    if(row<=0 or column<=0):
        raise Exception("Column and Row must be greater than 0")

    rowT=int(input(f"Choose a row to hide the treasure (1-{row}): "))
    columnT=int(input(f"Choose a column to hide the treasure (1-{column}): "))

    if (rowT <=0 or rowT>row or columnT<=0 or columnT>column):
        raise Exception("Enter a valid location, the treasure cannot be outside the dimensions of the board.")
    
    if (not row or not column or not rowT or not columnT) is int:
        raise ValueError

except ValueError as e:
    print(f"Error : => All values entered must be an integer.\n({e})")
except Exception as e:
    print(f"Error : => ({e})")

else:
    asyncio.run(load("Draw function"))

    #Player Guess
    win=play(row,column,rowT,columnT)
    if win:
        print("\nCongratulations...\n")

    print(f"Board{row,column}\nTreasure{rowT,columnT}")

finally:
  print("\nFinished...\n")