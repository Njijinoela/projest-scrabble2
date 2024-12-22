import unittest
from src.scrabble.rack.tile_bag import TileBag
from src.scrabble.rack.rack import Rack

class TestTileBag(unittest.TestCase):
    def setUp(self):
        self.tile_bag = TileBag()
    
    def test_initial_bag_size(self):
        self.assertEqual(self.tile_bag.remaining_tiles(), 100)
    
    def test_draw_tile(self):
        initial_count = self.tile_bag.remaining_tiles()
        tile = self.tile_bag.draw_tile()
        self.assertIsInstance(tile, str)
        self.assertEqual(self.tile_bag.remaining_tiles(), initial_count - 1)
    
    def test_draw_multiple_tiles(self):
        draw_count = 7
        initial_count = self.tile_bag.remaining_tiles()
        drawn_tiles = self.tile_bag.draw(draw_count)
        self.assertEqual(len(drawn_tiles), draw_count)
        self.assertEqual(self.tile_bag.remaining_tiles(), initial_count - draw_count)
    
    def test_tile_distribution(self):
        distribution = {
            'E': 12, 'A': 9, 'I': 9, 'O': 8, 'N': 6, 'R': 6, 'T': 6,
            'L': 4, 'S': 4, 'U': 4, 'D': 4, 'G': 3, 'B': 2, 'C': 2,
            'M': 2, 'P': 2, 'F': 2, 'H': 2, 'V': 2, 'W': 2, 'Y': 2,
            'K': 1, 'J': 1, 'X': 1, 'Q': 1, 'Z': 1, 'BLANK': 2
        }
        for letter, expected_count in distribution.items():
            self.assertEqual(self.tile_bag.tiles.count(letter), expected_count)

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
    
    def test_rack_tile_bag_integration(self):
        initial_bag_count = self.tile_bag.remaining_tiles()
        self.assertEqual(initial_bag_count, 93)  # 100 - 7 initial rack tiles

if __name__ == '__main__':
    unittest.main()
