from typing import List, Tuple, Optional

def create_board() -> List[List[str]]:
    """Create and return a 3x3 Tic-Tac-Tooe board."""
    return [[" " for _ in range(3) ] for _ in range(3)]

def print_board(board: List[List[str]]) -> None:
    """Prints the Tic-Tac-Toe Board"""

    for row in board:
        print("|".join(row))
        print("-----")

if __name__=='__main__':
    board = create_board()
    print_board(board)