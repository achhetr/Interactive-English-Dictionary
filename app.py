import json
from spellchecker import SpellChecker

# load data.json
data = json.load(open("data.json"))

# spell checker object
spell = SpellChecker()

# function to extract meaning of the word
def word_meaning(word):
    if word in data:
        meaning = data[word]
    elif spell.correction(word) in data: 
        print("\nOops we couldn't find '%s' but we found '%s' \n" % (word,spell.correction(word)))
        check_word = input("Press Y/N for Yes or No:  ")
        if(check_word.lower() == 'y'):
            meaning = data[spell.correction(word)]
        else:
            meaning = 'Word does not exits! Please double check it\n'
    else:
        meaning = 'Word does not exits! Please double check it\n'
    return meaning


# input user input
user_input = input("\nEnter word for meaning and press enter:  ")

# convert all input into lower case
result = word_meaning(user_input.lower())

# output

if result != 'Word does not exits! Please double check it\n':
    print("\nMeaning: \n")
    print("\n\n".join(result))
    print("\n")
else: 
    print("\n\n" + result)