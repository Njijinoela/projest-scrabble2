from random import choice
from typing import List, Dict

class TileBag:
    def __init__(self):
        # Initialize with exactly 100 tiles
        self.tiles = self._initialize_tiles()
    
    def _initialize_tiles(self):
        # Updated distribution to have exactly 100 tiles
        distribution = {
            'E': 12, 'A': 9, 'I': 9, 'O': 8, 'N': 6, 'R': 6, 'T': 6, 'L': 4, 
            'S': 4, 'U': 4, 'D': 4, 'G': 3, 'B': 2, 'C': 2, 'M': 2, 'P': 2,
            'F': 2, 'H': 2, 'V': 2, 'W': 2, 'Y': 2, 'K': 1, 'J': 1, 'X': 1,
            'Q': 1, 'Z': 1, 'BLANK': 2
        }
        tiles = []
        for letter, count in distribution.items():
            tiles.extend([letter] * count)
        return tiles
    
    def draw_tile(self) -> str:
        if not self.tiles:
            raise ValueError("Tile bag is empty")
        tile = choice(self.tiles)
        self.tiles.remove(tile)
        return tile
    
    def remaining_tiles(self):
        return len(self.tiles)

    def draw(self, count):
        """Draw specified number of tiles from the bag"""
        if count > len(self.tiles):
            count = len(self.tiles)
        drawn = self.tiles[:count]
        self.tiles = self.tiles[count:]
        return drawn
