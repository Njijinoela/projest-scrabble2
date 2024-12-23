
import unittest
from src.scrabble.rack.tile_bag import TileBag
from src.scrabble.rack.rack import Rack

class TestRack(unittest.TestCase):
    def setUp(self):
        self.tile_bag = TileBag()
        self.rack = Rack(self.tile_bag)
    
    def test_initial_rack_size(self):
        self.assertEqual(len(self.rack.get_tiles()), 7)
    
    def test_remove_tile(self):
        tiles = self.rack.get_tiles()
        tile_to_remove = tiles[0]
        self.assertTrue(self.rack.remove_tile(tile_to_remove))
        self.assertEqual(len(self.rack.get_tiles()), 6)
    
    def test_fill_rack(self):
        self.rack.remove_tile(self.rack.get_tiles()[0])
        self.rack.fill_rack()
        self.assertEqual(len(self.rack.get_tiles()), 7)

if __name__ == '__main__':
    unittest.main()
