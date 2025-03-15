from typing import List, Tuple, Optional

def create_board() -> List[List[str]]:
    """Create and return a 3x3 Tic-Tac-Tooe board."""
    return [[" " for _ in range(3) ] for _ in range(3)]

def print_board(board: List[List[str]]) -> None:
    """Prints the Tic-Tac-Toe Board"""

    for row in board:
        print("|".join(row))
        print("-----")

def is_move_valid(board: List[List[str]], row: int, col: int)-> bool:
    """"Checks if the given move is valid or not"""
    return board[row][col]==' '

def make_move(board: List[List[str]], row: int, col: int, player) -> None:
    """Place the player's symbol (either X or 0) at a given postition"""
    board[row][col] = player

def is_winner(board: List[List[str]], player: str) -> bool:
    """Check if the given player has won the game"""    
    for i in range(3):
        if all([cell==player for cell in board[i]]) or all([board][j][i] == player for j i):
            return True
        if (board[0][0] == board [1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0]== player):
            return True

def is_game_over(board[List[List[str]]]) -> bool:
    """Check if the game is over(Either one player wins or its a draw)"""
    return is_winner(board, player='X') or is winner(board, player='O') or all(" " not in a row for row in board)

def minimax(board: List[List[str]], depth: int, maximizing_player:bool)-> int:
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
         best_score = float('-inf')
         for row in range(3):
            for col in range(3):
                if is_move_valid(board, row, col):
                    board[row][col] = "X"
                    score = minimax(board, depth+1, False)
                    board[row][col] = " "    
                    best_score = max(score, best_score)
    return best_score
                           






if __name__=='__main__':
    board = create_board()
    print_board(board)