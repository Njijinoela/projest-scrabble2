from typing import List
from .tile_bag import TileBag

class Rack:
    def __init__(self, tile_bag: TileBag):
        self.tile_bag = tile_bag
        self.tiles: List[str] = []
        self.fill_rack()
    
    def fill_rack(self):
        while len(self.tiles) < 7 and self.tile_bag.remaining_tiles() > 0:
            self.tiles.append(self.tile_bag.draw_tile())
    
    def remove_tile(self, tile):
        if tile in self.tiles:
            self.tiles.remove(tile)
            return True
        return False
    
    def get_tiles(self) -> List[str]:
        return self.tiles.copy()

def exchange_tiles(self, tiles_to_exchange):
    # Remove exchanged tiles from rack
    for tile in tiles_to_exchange:
        if tile in self.tiles:
            self.tiles.remove(tile)
            self.tile_bag.tiles.append(tile)
    
    # Draw new tiles to maintain 7 tiles
    while len(self.tiles) < 7 and self.tile_bag.remaining_tiles() > 0:
        new_tile = self.tile_bag.draw_tile()
        self.tiles.append(new_tile)
    self.tiles.extend(new_tiles)