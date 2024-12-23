# Function to validate words using a dictionary file
def dictionary(word):
    
    try:
        with open('dict.txt', 'r') as file:
            # Read the file and create a set of words for quick lookup
            word_set = set(file.read().splitlines())
        return word.lower() in word_set
    except FileNotFoundError:
        print("Error: The file 'dict.txt' was not found.")
        return False

dictionary()