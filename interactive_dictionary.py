#import the necessary library
import json
from difflib import get_close_matches

#load the json file which contains the words and their meaning
data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        suggestion = input("Did you mean %s instead? Enter Y if yes or N if no:\n" % get_close_matches(word, data.keys())[0])
        suggestion = suggestion.lower()
        if suggestion == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif suggestion == "n":
            print(f"Sorry! The word {word} doesn't exist. Please double check it.")
        else:
            print("We didn't understand your entry!")

    else:
        print(f"Sorry! The word {word} doesn't exist. Please double check it.")

print("\n*****Welcome to the Central Dictionary*****\n")
while(True):
    word = input("Enter the word:\n")
    output = translate(word)
    if type(output) == list:
        for i in output:
            print("*"+ i)
    else:
        print(output)


