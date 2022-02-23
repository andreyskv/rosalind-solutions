#sudoku = '000007009000080060400200500000009008000060070030100200016400300543000000200000000'
#sudoku = '200800009607901000000062008000000910002307800013000000800230000000508307300006005'
sudoku = '530070000600195000098000060800060003400803001700020006060000280000419005000080079'


#[["5","3",".",".","7",".",".",".","."],
# ["6",".",".","1","9","5",".",".","."],
# [".","9","8",".",".",".",".","6","."],
# ["8",".",".",".","6",".",".",".","3"],
# ["4",".",".","8",".","3",".",".","1"],
# ["7",".",".",".","2",".",".",".","6"],
# [".","6",".",".",".",".","2","8","."],
# [".",".",".","4","1","9",".",".","5"],
# [".",".",".",".","8",".",".","7","9"]]


N = 9
iterations = 0
board = []

#Transform sudoku string into 2d array board
for p in range(1, N + 1):
    row = [int(q) for q in list(sudoku[(p - 1) * N:p * N])]
    print(row)
    board.append(row)


def is_valid(y, x, val):
    global iterations
    iterations += 1
    #Check the row x not having val
    if val in board[x]:
        return False

    #Check the column y not having val
    if val in [col[y] for col in board]:
        return False

    #Find top left coords of the 3x3 square
    xc = (x // 3) * 3
    yc = (y // 3) * 3
    #Check if the square contains val
    for col in board[xc:xc + 3]:
        if val in col[yc:yc + 3]:
            return False

    return True


def solve():
    for j in range(0, N):
        for i in range(0, N):
            if board[j][i] != 0:
                continue
            for val in range(1, N + 1):
                if is_valid(i, j, val):
                    board[j][i] = val
                    if not solve():
                        board[j][i] = 0
                    else:
                        return True
            return False
    return True


solve()
print()
for h in range(0, N):
    print(board[h])

print("iterations = ", iterations)