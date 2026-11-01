
N = int(input("Enter N :"))

# Create an empty chessboard
board = [[0 for j in range(N)] for i in range(N)]

# Place first Queen at row 0, column 1
board[0][0] = 1


# Check whether a position is safe
def is_safe(board, row, col):

    # Check column above
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


# Solve N-Queens using Backtracking
def solve_nqueens(board, row):

    if row == N:
        return True

    for col in range(N):

        if is_safe(board, row, col):

            board[row][col] = 1

            if solve_nqueens(board, row + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Display chessboard
def print_board(board):

    for i in range(N):
        for j in range(N):

            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print("-", end=" ")

        print()


# Main program
print("Initial Chessboard:")
print_board(board)

if solve_nqueens(board, 1):

    print("\nFinal N-Queens Solution:")
    print_board(board)

else:
    print("\nNo solution exists.")
