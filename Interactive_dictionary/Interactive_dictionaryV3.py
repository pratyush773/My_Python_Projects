import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:   # Checks for nouns like Dehli, Paris
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes or N for no !" % get_close_matches(word, data.keys())[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "Word doesn't exists, kindly check and enter correct word!"
        else:
            return "We donot undertstand you input"
    else:
        return "Word doesn't exists, kindly check and enter correct word!"


word = input("Enter word :")
output = (translate(word))

if type(output) == list:
    for i in range(len(output)):
        print(output[i])
else:
    print(output)