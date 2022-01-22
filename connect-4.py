from termcolor import colored, cprint
print_red = lambda x: cprint(x, 'red')
print_yellow = lambda x: cprint(x, 'yellow')

class Board:
    def __init__(self, no_rows, no_columns):
        print("Initialising board...")
        self.rows = no_rows
        self.columns = no_columns
        self.board_spaces = [["X" for i in range(self.columns)] for j in range(self.rows)]

    def print_board(self):
        for row in self.board_spaces:
            for elem in row:
                print(elem, end=' ')
            print('\n')



print("""

░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗░█████╗░████████╗  ░░██╗██╗
██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗╚══██╔══╝  ░██╔╝██║
██║░░╚═╝██║░░██║██╔██╗██║██╔██╗██║█████╗░░██║░░╚═╝░░░██║░░░  ██╔╝░██║
██║░░██╗██║░░██║██║╚████║██║╚████║██╔══╝░░██║░░██╗░░░██║░░░  ███████║    ( ͡° ͜ʖ ͡°( ಠ ͜ʖ ಠ ) ͡° ͜ʖ ͡°)
╚█████╔╝╚█████╔╝██║░╚███║██║░╚███║███████╗╚█████╔╝░░░██║░░░  ╚════██║
░╚════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝░╚════╝░░░░╚═╝░░░  ░░░░░╚═╝

""")

print("Welcome to Connect 4.")
player_1 = input("Player 1 please enter cool gamer tag: ")
player_2 = input("Player 2 please enter cool gamer tag: ")
r_and_c = input("Please enter number of rows and columns the board should have, separated by a space: ")
r_and_c_list = r_and_c.split()
r = int(r_and_c_list[0])
c = int(r_and_c_list[1])

board1 = Board(r, c)
board1.print_board()
