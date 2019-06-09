class Player: # Class for players
    def __init__(self):
        self.choice = ''


def makeGrid():
    grid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    askingforXorO(grid)
    print("Final Result")
    printgrid(grid)


def askingforXorO(grid):
    player1 = Player() # assigning players
    player2 = Player()
    run = True
    while run:
        choice = input("Please choose either X or O?\n") # asking and assigning x and o to players
        choice = choice.upper()
        if (choice == 'X'):
            player1.choice = 'X'
            player2.choice = 'O'

        elif (choice == 'O'):
            player1.choice = 'O'
            player2.choice = 'X'

        else:
            print("Please make a valid choice")

        printgrid(grid)
        endgame = False
        for n, i in enumerate(grid):
            if (endgame == True):
                print("End Game")
                run = False
                break
            while (grid[n] == 'X' or 'O'):

                if (n % 2 == 0):            # using prime numbers logic to assign turns
                    var1 = player1.choice
                else:
                    var1 = player2.choice

                repeat = True
                while repeat:
                    userinput = int(input(f"\nEnter where you want to place {var1}\n"))

                    if (userinput):

                        try:
                            grid.remove(str(userinput))
                            repeat = False
                        except ValueError:
                            print("This space is already full or doesn't exist.\n Try again")
                            repeat = True



                grid.insert(userinput - 1, var1)

                printgrid(grid)

                if (check_winner(grid, var1)):
                    endgame = True
                    break
                break
        print("Draw, No one won")
        run = False
# if (grid[n] != 'X' or 'O'):
#     print("Draw")
#     break


def check_winner(grid, variable): # checking winner
    win_commbinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for j, k, l in win_commbinations:
        if (grid[j] == grid[k] == grid[l] == variable):
            print(f"Player with {variable} won")
            return True


def printgrid(grid): # printing grid
    printgrid = (
        f"{grid[0]} | {grid[1]} | {grid[2]}\n{grid[3]} | {grid[4]} | {grid[5]} \n{grid[6]} | {grid[7]} | {grid[8]}")
    #  printinggrid1 = (grid[0]+ "|" + grid[1]+ "|" + grid[2] + "|")
    #  printinggrid2 = ("\n" + grid[3] + "|" +  grid[4] +"|" +  grid[5] + "|")
    #  printinggrid3 = ("\n" + grid[6]+ "|" +  grid[7] +"|" +  grid[8] + "|")
    #  print(printinggrid1, printinggrid2, printinggrid3)
    print(printgrid)

while True:

    if input("Start Tic Tac Toe(y/n)\n") == 'y': # asking user to play tic-tac-toe
            makeGrid()
            break
    else:
        print("_____Exiting_____")
        break;

