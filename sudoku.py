sud = [
    [1,2,0,4,5,0,7,8,0],
    [1,2,0,4,5,0,7,8,0],
    [1,2,0,4,5,0,7,8,0],
    [1,2,0,4,5,0,7,8,0],
    [1,2,0,4,5,0,7,8,0],
    [1,2,0,4,5,0,7,8,0],
    [1,2,0,4,5,0,7,8,0],
    [1,2,0,4,5,0,7,8,0],
    [1,2,0,4,5,0,7,8,0],   
]

def build_board(board):

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("_ _ _ _ _ _ _ _ _ _ _ _ _ ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    for i in range(0, len(board), 1):
        for j in range(0, len(board), 1):
            if board[i][j] == 0:
                return (i, j)
    return None

build_board(sud)
