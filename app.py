import json

# load data.json
data = json.load(open("data.json"))

# function to extract meaning of the word
def word_meaning(word):
    if word in data:
        meaning = data[word]
    else:
        meaning = 'Word does not exits!'
    return meaning

# input user input
user_input = input("Enter word for meaning and press enter: ")

# print result
result = word_meaning(user_input)
if result:
    print(result)
else:
    print("word does not exist")