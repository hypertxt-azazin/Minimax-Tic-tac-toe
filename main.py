from typing import List, Tuple, Optional

def create_board() -> List[List[str]]:
    """Create and return a 3x3 Tic-Tac-Toe board."""
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board: List[List[str]]) -> None:
    """Prints the Tic-Tac-Toe Board with better formatting"""
    for i, row in enumerate(board):
        print(" | ".join(row))  # Print each row with separators
        if i < 2:  # Only print horizontal lines between rows
            print("---------")


def is_move_valid(board: List[List[str]], row: int, col: int)-> bool:
    """Checks if the given move is valid or not"""
    return board[row][col]==' '

def make_move(board: List[List[str]], row: int, col: int, player) -> None:
    """Place the player's symbol (either X or O) at a given position"""
    board[row][col] = player

def is_winner(board: List[List[str]], player: str) -> bool:
    """Check if the given player has won the game"""
    for i in range(3):
        if all([cell==player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if (board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player):
        return True
    
def is_game_over(board: List[List[str]]) -> bool:
    """Check if the game is Over(Either one player wins or it is a draw)"""
    return is_winner(board, player='X') or is_winner(board, player='O') or all(" " not in row for row in board)

def minimax(board: List[List[str]], depth: int, maximizing_player: bool) -> int:
    if is_winner(board, "X"):
        return -1
    if is_winner(board, "0"):
        return 1
    if is_game_over(board):
        return 0
    
    if maximizing_player:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if is_move_valid(board, row, col):
                    board[row][col] = "0"
                    score = minimax(board, depth+1, False)
                    board[row][col] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if is_move_valid(board, row, col):
                    board[row][col] = "X"
                    score = minimax(board, depth+1, True)
                    board[row][col] = " "
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board: List[List[str]]) -> Tuple[int, int]:
    best_score = float('-inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if is_move_valid(board, row, col):
                board[row][col] = "0"
                score = minimax(board, 0, False)
                board[row][col] = " "
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

def play_game() -> None:
    """Main function"""
    board = create_board()
    current_player = 'X'
    print_board(board)
    while not is_game_over(board):
        if current_player == 'X':
            row, col = map(int, input('Enter row and col (0 2) seperated by space: ').split())
        else: # AI's turn
            row, col = find_best_move(board)
            print(f"AI's move: {row}, {col}")

        if is_move_valid(board, row, col):
            make_move(board, row, col, current_player)
            print_board(board)
            if is_winner(board, current_player):
                print(f"{current_player} wins")
                break

            current_player = "0" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again")
    else:
        print("Its a tie")



if __name__=='__main__':
    play_game()