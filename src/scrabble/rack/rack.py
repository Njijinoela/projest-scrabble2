from typing import List
from .tile_bag import TileBag

class Rack:
    def __init__(self, tile_bag: TileBag):
        self.tile_bag = tile_bag
        self.tiles: List[str] = []
        self.fill_rack()
    
    def fill_rack(self) -> None:
        while len(self.tiles) < 7 and self.tile_bag.remaining_tiles() > 0:
            self.tiles.append(self.tile_bag.draw_tile())
    
    def remove_tile(self, tile: str) -> bool:
        if tile in self.tiles:
            self.tiles.remove(tile)
            return True
        return False
    
    def get_tiles(self) -> List[str]:
        return self.tiles.copy()
