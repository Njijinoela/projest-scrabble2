import unittest
from src.scrabble.rack.tile_bag import TileBag

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
    
    def test_empty_bag(self):
        # Draw all tiles
        initial_count = self.tile_bag.remaining_tiles()
        drawn_tiles = self.tile_bag.draw(initial_count)
        self.assertEqual(len(drawn_tiles), initial_count)
        self.assertEqual(self.tile_bag.remaining_tiles(), 0)
        
        # Test drawing from empty bag
        with self.assertRaises(ValueError):
            self.tile_bag.draw_tile()
    
    def test_tile_distribution(self):
        all_tiles = self.tile_bag.tiles
        distribution = {
            'E': 12, 'A': 9, 'I': 9, 'O': 8, 'N': 6, 'R': 6, 'T': 6,
            'L': 4, 'S': 4, 'U': 4, 'D': 4, 'G': 3, 'B': 2, 'C': 2,
            'M': 2, 'P': 2, 'F': 2, 'H': 2, 'V': 2, 'W': 2, 'Y': 2,
            'K': 1, 'J': 1, 'X': 1, 'Q': 1, 'Z': 1, 'BLANK': 2
        }
        
        for letter, expected_count in distribution.items():
            actual_count = all_tiles.count(letter)
            self.assertEqual(actual_count, expected_count)

if __name__ == '__main__':
    unittest.main()
