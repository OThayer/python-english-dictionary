import json

data = json.load(open("data.json"))

def define(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "That word doesn't exist. Please check your spelling."

word = input("Enter word: ")

print(define(word))