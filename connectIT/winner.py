def check_winner(board, row, col, piece):

    row_list = board[row]
    row_indices = [i for i, x in enumerate(row_list) if x == piece]
    index_len = len(row_indices)
    if(index_len == 4  and (row_indices[-1] - row_indices[0] == 3)):
        return True
    elif( row >= 3):
        col_list= [i[col] for i in board]
        map(int, col_list)
        col_indices = [i for i, x in enumerate(col_list) if x == piece]
        if(len(col_indices) == 4  and (col_indices[-1] - col_indices[0] == 3)):
           return True

    else:
        return False

