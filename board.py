def create_board():
    board = [[' ' for _ in range(15)] for _ in range(15)]

    SPECIAL_TILES = {
        "TW": [(0, 0), (0, 7), (0, 14), (7, 0), (7, 14), (14, 0), (14, 7), (14, 14)],
        "DW": [
            (1, 1), (1, 13), (2, 2), (2, 12), (3, 3), (3, 11), (4, 4), (4, 10), (7, 7),
            (10, 4), (10, 10), (11, 3), (11, 11), (12, 2), (12, 12), (13, 1), (13, 13)
        ],
        "TL": [
            (1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13),
            (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)
        ],
        "DL": [
            (0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), 
            (6, 2), (6, 6), (6, 8), (6, 12), (7, 3), (7, 11), (8, 2), 
            (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), 
            (12, 6), (12, 8), (14, 3), (14, 11)
        ]
    }

    # Place each type of special tile at its respective coordinates
    for tile_type, positions in SPECIAL_TILES.items():
        for row, col in positions:
            board[row][col] = tile_type

    # Center star tile
    board[7][7] = "*"
    print("\nDebug: Special tiles added to the board.")    

    return board

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 63)

if __name__ == "__main__":
    board = create_board()
    print_board(board)