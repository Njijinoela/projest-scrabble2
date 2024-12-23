class Player:
    def __init__(self, name):
        self.name = name
        self.tiles = []  # The player's tiles
        self.score = 0   # The player's score

    def draw_tiles(self, tile_bag, num_tiles):
        """Draw tiles from the tile bag."""
        for _ in range(num_tiles):
            if tile_bag:
                self.tiles.append(tile_bag.pop())  # Draw a tile from the bag if not empty
            else:
                break

    def play_word(self, word):
        """Play a word by removing used tiles from the player's rack."""
        if self.can_play_word(word):
            self.remove_tiles(word)
            print(f"{self.name} played the word '{word}'")
            return True
        else:
            print(f"{self.name} cannot play the word '{word}'")
            return False

    def can_play_word(self, word):
        """Check if the player has the tiles to play a word."""
        available_tiles = self.tiles[:]
        for letter in word:
            if letter in available_tiles:
                available_tiles.remove(letter)
            else:
                return False
        return True

    def remove_tiles(self, word):
        """Remove tiles used to play a word from the player's rack."""
        for letter in word:
            if letter in self.tiles:
                self.tiles.remove(letter)

    def add_score(self, points):
        """Add points to the player's score."""
        self.score += points
        print(f"{self.name} scored {points} points. Total: {self.score}")

