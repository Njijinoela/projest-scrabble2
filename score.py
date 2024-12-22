def calculate_scrabble_score(word):
    #letter values

    letter_values = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
        'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
        'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
    }

    if not isinstance(word, str) or not word:
        raise ValueError("Invalid input: Please provide a valid string.")
    
    word = word.upper()

    total_score = 0
    for letter in word:
        if letter in letter_values:
            total_score += letter_values[letter]
        else:
            raise ValueError(f"Invalid character '{letter}' in the word.")

    return total_score

if __name__ == "__main__":
    try:
        word = "scrabble"
        score = calculate_scrabble_score(word)
        print(f"The score for the word '{word}' is: {score}")
    except ValueError as e:
        print(e)
