def is_valid(board):
    # row validation
    for row in board:
        seen = set()
        for cell in row:
            if cell != 0:
                if cell in seen:
                    return False
                seen.add(cell)

    # column validation
    for col in range(9):
        seen = set()
        for row in range(9):
            cell = board[row][col]
            if cell != 0:
                if cell in seen:
                    return False
                seen.add(cell)

    # slice validation
    for i in range(3):
        for j in range(3):
            seen = set()
            for p in range(3 * i, 3 * i + 3):
                for q in range(3 * j, 3 * j + 3):
                    cell = board[p][q]
                    if cell != 0:
                        if cell in seen:
                            return False
                        seen.add(cell)

    # no inconsistency found
    return True


def get_possibilities(board, row, col):
    ret = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    invalid = set()

    for i in range(9):
        invalid.add(board[row][i])

    for j in range(9):
        invalid.add(board[j][col])

    slice_r = (row // 3) * 3
    slice_c = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            invalid.add(board[slice_r + i][slice_c + j])

    return ret - invalid


def solver(board):
    print("call")
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for x in get_possibilities(board, i, j):
                    board[i][j] = x
                    solver(board)
                    board[i][j] = 0
            return
