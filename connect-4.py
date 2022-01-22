from termcolor import colored, cprint
print_red = lambda x: cprint(x, 'red', end=" ")
print_yellow = lambda x: cprint(x, 'yellow',end=" ")

class Board:
    def __init__(self, no_rows, no_columns):
        print("Initialising board... \n")
        self.rows = no_rows
        self.columns = no_columns
        self.board_spaces = [[0 for i in range(self.columns)] for j in range(self.rows)]

    def print_board(self):
        for row in self.board_spaces:
            for elem in row:
                if elem == 0:
                    print("X", end=" ")
                elif elem == 1:
                    print_red("X")
                else:
                    print_yellow("X")
            print('\n')
        for i in range(self.columns):
            print(i+1, end=' ')
        print('\n')



print("""

#####                                                     
#     #    ####   #    #  #    #  ######   ####   #####    #    #  
#         #    #  ##   #  ##   #  #       #    #    #      #    #  
#         #    #  # #  #  # #  #  #####   #         #      #    #  
#         #    #  #  # #  #  # #  #       #         #      ####### 
#     #   #    #  #   ##  #   ##  #       #    #    #           #  
 #####     ####   #    #  #    #  ######   ####     #           #  

""")

print("Welcome to Connect 4.")
player_1 = input("Player 1 please enter cool gamer tag: ")
player_2 = input("Player 2 please enter cool gamer tag: ")
r = int(input("Please enter number of rows the board should have: "))
c = int(input("Please enter number of columns the board should have: "))
board1 = Board(r, c)
board1.print_board()
print("This is your board. ")
print_red(player_1)
print("you are with red")
print_yellow(player_2)
print("you are with yellow \n")

round = 0
game_over = False

while not game_over:
    round += 1
    if round % 2 == 1:
        print_red(player_1)
        print("it's your turn!", end=' ')
        selected_column = int(input("Select a column to make your move: ")) - 1
        while selected_column < 0 or selected_column > board1.columns-1 or board1.board_spaces[0][selected_column] is not 0:
           print("Invalid column.")
           selected_column = int(input("Select a column to make your move: ")) - 1
        row = 0
        while(row < board1.rows - 1 and board1.board_spaces[row+1][selected_column] == 0):
            row += 1
        board1.board_spaces[row][selected_column] = 1
        board1.print_board()
    else:
        print_yellow(player_2)
        print("it's your turn!", end=' ')
        selected_column = int(input("Select a column to make your move: ")) - 1
        while selected_column < 0 or selected_column > board1.columns-1 or board1.board_spaces[0][selected_column] is not 0:
           print("Invalid column.")
           selected_column = int(input("Select a column to make your move: ")) - 1
        row = 0
        while(row < board1.rows - 1 and board1.board_spaces[row+1][selected_column] == 0):
            row += 1
        board1.board_spaces[row][selected_column] = 2
        board1.print_board()

