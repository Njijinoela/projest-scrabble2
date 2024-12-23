
# Projest-Scrabble2 Rack Generator

A specialized tool for generating Scrabble letter racks.

## Rack Generator Features

- Randomly selects 7 letters for the player's rack
- Maintains proper letter distribution based on official Scrabble rules
- Handles vowel and consonant balance
- Updates rack after letters are played

## Letter Distribution

The rack generator follows standard Scrabble letter frequencies:
- Common letters (E, A, I, O, N, R, T, L, S) appear more frequently
- Less common letters (Q, Z, J, X) appear less frequently
- Total of 100 tiles in the complete set

## Usage Example

The rack generator creates a new rack of 7 letters:

```python
rack = generate_rack()  # Returns something like ['A', 'E', 'I', 'N', 'S', 'T', 'R']
# projest-scrabble2