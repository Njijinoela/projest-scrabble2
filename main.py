import random
from itertools import combinations

# Constants for the tile bag and letter points
TILE_BAG = {
    "A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, "H": 2, "I": 9,
    "J": 1, "K": 1, "L": 4, "M": 2, "N": 6, "O": 8, "P": 2, "Q": 1, "R": 6,
    "S": 4, "T": 6, "U": 4, "V": 2, "W": 2, "X": 1, "Y": 2, "Z": 1, "@": 2
}

LETTER_POINTS = {
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1,
    "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1,
    "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10, "@": 0
}

# Function to draw tiles from the tile bag
def draw_tiles(tile_bag, num=7):
    tiles = []
    for _ in range(num):
        if not tile_bag:
            break
        tile = random.choice(list(tile_bag.keys()))
        tiles.append(tile)
        tile_bag[tile] -= 1
        if tile_bag[tile] == 0:
            del tile_bag[tile]
    return tiles

# Function to display the game board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (len(board[0]) * 4 - 1))

# Function to validate words using a dictionary file
def dictionary(word):
    try:
        with open('/home/njiji/Developments/code/phase3/projest-scrabble2/dict.txt', 'r') as file:
            # Load words into a set for quick lookup
            word_set = {line.strip().lower() for line in file}
        return word.lower() in word_set
    except FileNotFoundError:
        print("Error: The file 'dict.txt' was not found.")
        return False

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.tiles = []  # The player's tiles
        self.score = 0   # The player's score

    def draw_tiles(self, tile_bag, num_tiles):
        new_tiles = draw_tiles(tile_bag, num_tiles)
        self.tiles.extend(new_tiles)

    def play_word(self, word, position, direction, board, tile_bag):
        if self.can_play_word(word):
            if self.place_word_on_board(word, position, direction, board):
                self.remove_tiles(word)
                points = calculate_scrabble_score(word)
                self.add_score(points)
                print(f"{self.name} played the word '{word}' for {points} points.")
                self.draw_tiles(tile_bag, 7 - len(self.tiles))  # Replenish tiles
                return True
        print(f"{self.name} cannot play the word '{word}'")
        return False

    def can_play_word(self, word):
        available_tiles = self.tiles[:]
        for letter in word:
            if letter in available_tiles:
                available_tiles.remove(letter)
            else:
                return False
        return True

    def remove_tiles(self, word):
        for letter in word:
            if letter in self.tiles:
                self.tiles.remove(letter)

    def add_score(self, points):
        self.score += points
        print(f"{self.name} scored {points} points. Total: {self.score}")

    def place_word_on_board(self, word, position, direction, board):
        row, col = position
        if direction not in ['H', 'V']:
            print("Invalid direction. Use 'H' for horizontal or 'V' for vertical.")
            return False

        # Validate the word placement
        for i, letter in enumerate(word):
            if direction == 'H':
                if col + i >= len(board[0]) or (board[row][col + i] != ' ' and board[row][col + i] != letter):
                    return False
            elif direction == 'V':
                if row + i >= len(board) or (board[row + i][col] != ' ' and board[row + i][col] != letter):
                    return False

        # Place the word
        for i, letter in enumerate(word):
            if direction == 'H':
                board[row][col + i] = letter
            elif direction == 'V':
                board[row + i][col] = letter
        return True

# Function to calculate the Scrabble score of a word
def calculate_scrabble_score(word):
    word = word.upper()
    return sum(LETTER_POINTS.get(letter, 0) for letter in word)


def computer_move(computer, board, dictionary_func):
    # Extract letters from the computer's rack
    rack_letters = computer.tiles
    board_letters = [board[row][col] for row in range(len(board)) for col in range(len(board[0])) if board[row][col] != ' ']

    # Combine rack letters with letters from the board
    for board_letter in board_letters:
        virtual_rack = rack_letters + [board_letter]

        # Generate combinations of letters to form words
        for word_length in range(2, len(virtual_rack) + 1):  # Words must be at least 2 letters
            for combination in combinations(virtual_rack, word_length):
                word = ''.join(combination)  # Form a potential word
                if dictionary_func(word):  # Check if the word is valid
                    # Attempt to place the word on the board
                    for row in range(len(board)):
                        for col in range(len(board[0])):
                            for direction in ['H', 'V']:
                                # Test placing the word
                                if computer.place_word_on_board(word, (row, col), direction, board):
                                    computer.remove_tiles(word)  # Remove used tiles
                                    points = calculate_scrabble_score(word)
                                    computer.add_score(points)
                                    print(f"The computer played the word '{word}' at ({row}, {col}) in direction '{direction}' for {points} points.")
                                    return True
    print("Computer could not find a valid move.")
    return False

# Main game loop with computer logic
def main():
    board = [[' ' for _ in range(15)] for _ in range(15)]
    tile_bag = TILE_BAG.copy()
    player1 = Player("Player 1")
    computer = Player("Computer")

    player1.draw_tiles(tile_bag, 7)
    computer.draw_tiles(tile_bag, 7)

    current_player = player1
    while tile_bag or any(player.tiles for player in [player1, computer]):
        print(f"\n{current_player.name}'s turn")
        display_board(board)
        print(f"Your tiles: {', '.join(current_player.tiles)}" if current_player == player1 else "")

        if current_player == player1:
            try:
                word = input("Enter a word to play: ").upper()
            except EOFError:
                print("\nEnd of input detected. Exiting the game.")
                break

            if not dictionary(word):
                print("Invalid word. Try again.")
                continue

            # Validate position
            while True:
                try:
                    position_input = input("Enter the starting position (row, col): ")
                    position = tuple(map(int, position_input.split(',')))
                    if len(position) != 2:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Please enter the position in the format 'row,col' (e.g., 7,8).")
                except EOFError:
                    print("\nEnd of input detected. Exiting the game.")
                    return

            # Validate direction
            while True:
                try:
                    direction = input("Enter direction ('H' for horizontal, 'V' for vertical): ").upper()
                    if direction in ['H', 'V']:
                        break
                    print("Invalid direction. Please enter 'H' or 'V'.")
                except EOFError:
                    print("\nEnd of input detected. Exiting the game.")
                    return

            if current_player.play_word(word, position, direction, board, tile_bag):
                current_player = computer
            else:
                print("Invalid move. Try again.")
        else:
            # Computer's turn
            if not computer_move(computer, board, dictionary):
                print("Computer passes its turn.")
            current_player = player1

    print("Game over!")
    print(f"{player1.name} Score: {player1.score}")
    print(f"{computer.name} Score: {computer.score}")
    if player1.score > computer.score:
        print(f"{player1.name} wins!")
    elif computer.score > player1.score:
        print(f"{computer.name} wins!")
    else:
        print("It's a tie!")

main()
