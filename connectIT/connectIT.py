import numpy as np
import winner


ROW_COUNT =6
COLUMN_COUNT =7
game_over = False
player = 1

def create_board():
    board = np.zeros((6,7))
    return board

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col]==0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def print_board(board):
    print(np.flip(board, 0))
    
def player_input(player):
    do = True
    while do:
        print("player {} make your selection (0 - 6 )".format(player),end='')
        col = int(input(""))
        if col in range (0,7):
            do = False
        else:
            print("invalid secection -  try again")
    return col

board = create_board()

while not game_over:
    print('\n')
    print_board(board)
    

    #ask player 1 to input
    col = player_input(player)
    #print(col)   
    if is_valid_location(board, col):
        row = get_next_open_row(board, col)
        drop_piece(board, row,col, player)
        #ckeck_for_connected(board, row, col, player)
        #print_board(board)
        result= winner.check_winner(board, row,col, player)
        if result == True:
            print_board(board)
            print("\nPlay {} won the game \n\n".format(player))
            
            game_over = True
            break

     
    if (player == 1):
        player =2

    else:
        player =1
        
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


