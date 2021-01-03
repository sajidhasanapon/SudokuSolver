def check_input(board, colors):
    red = (255, 0, 0)
    blue = (0, 0, 255)
    is_invalid_input = False

    for i in range(9):
        for j in range(9):
            colors[i][j] = blue

    # row validation
    for r in range(9):
        for i in range(8):
            for j in range(i+1, 9):
                if board[r][i] != 0:
                    if board[r][i] == board[r][j]:
                        colors[r][i] = red
                        colors[r][j] = red
                        is_invalid_input = True

    # column validation
    for c in range(9):
        for i in range(8):
            for j in range(i+1, 9):
                if board[i][c] != 0:
                    if board[i][c] == board[j][c]:
                        colors[i][c] = red
                        colors[j][c] = red
                        is_invalid_input = True

    # slice validation
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                rr = (i // 3) * 3
                cc = (j // 3) * 3
                for p in range(rr, rr + 3):
                    for q in range(cc, cc + 3):
                        if i != p and j != q:
                            if board[i][j] == board[p][q]:
                                colors[i][j] = red
                                colors[p][q] = red
                                print("s", i, j, p, q)
                                is_invalid_input = True

    return is_invalid_input

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


def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for x in get_possibilities(board, i, j):
                    board[i][j] = x
                    if solve(board):
                        return True
                board[i][j] = 0
                return False

    return True
