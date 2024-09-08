import json
import difflib

# Load the data from the json file
def load_dictionary(fileName):
    with open(fileName, "r") as fileData:
        return json.load(fileData)
    
data = load_dictionary("data.json") 

# function for if a word is not found in the dictionary or misspelled
def suggestedWord(word):
    word = word.lower()
    suggestions = difflib.get_close_matches(word, data.keys())
    if suggestions:
        return f'Did you mean {suggestions[0]} instead of {word}?'
    else:
        return f'The word {word} does not exist in the dictionary.'

# function that return a definition of a word
def getDefinition(word):
    word = word.lower()
    if word in data:
        return data[word]
    else: 
        suggestions = suggestedWord(word)
        return f'{suggestions} Please try again.'
    
# function that returns a list of all the words in the dictionary
def getAllWords():
    return list(data.keys())

def main():
    word = input('Enter a word: ')
    output = getDefinition(word)
    print(output)

if __name__ == "__main__":
    main()