class Player:
    def __init__(self, name):
        self.name = name
        self.tiles = []  # The player's tiles
        self.score = 0   # The player's score

    def draw_tiles(self, tile_bag, num_tiles):
        
        for _ in range(num_tiles):
            if tile_bag:
                self.tiles.append(tile_bag.pop())  # Draw a tile from the bag if not empty
            else:
                break

    def play_word(self, word):
        
        if self.can_play_word(word):
            self.remove_tiles(word)
            print(f"{self.name} played the word '{word}'")
            return True
        else:
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

