from itertools import combinations

def computerMove(computer_rack, board_letters, dictionary):

    # Extract letters from the rack
    rack_letters = [tile['letter'] for tile in computer_rack]
    
    # Combine rack letters with each letter from the board
    for board_letter in board_letters:
        # Create a virtual rack (rack + one letter from the board)
        virtual_rack = rack_letters + [board_letter]
        
        # Generate all possible combinations of letters from the virtual rack of varying lengths
        for word_length in range(2, len(virtual_rack) + 1):  # Words must be at least 2 letters
            for combination in combinations(virtual_rack, word_length):
                word = ''.join(combination)  # Join the combination to form a word
                # Check if the word exists in the dictionary
                if word in dictionary:
                    return word  # Return the first valid word
    
    # If no valid word is found
    return None
