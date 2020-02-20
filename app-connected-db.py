from spellchecker import SpellChecker
import mysql.connector


def query_sent(q):
    sql_query = "SELECT * FROM Dictionary WHERE Expression = '%s'" % q
    cursor = con.cursor()
    query = cursor.execute(sql_query)
    results = cursor.fetchall()
    output = []
    if results:
        for result in results:
            output.append(result[1])
        return output
    else:
        return ""


# function to extract meaning of the word
# load data from database
def word_meaning(word):
    meaning = query_sent(word)
    if not meaning:
        meaning = query_sent(spell.correction(word))
        if meaning:
            print("\nOops we couldn't find '%s' but we found '%s' \n" % (word,spell.correction(word)))
            check_word = input("Press Y/N for Yes or No:  ")
            if not check_word.lower() == 'y':
                print("\nTry again!!")
                meaning = ""
        else: 
            meaning = ""
    return meaning


# input user input
user_input = input("\nEnter word for meaning and press enter:  ")

# connect to db
con = con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
    )

# spell checker object
spell = SpellChecker()

# convert all input into lower case
result = word_meaning(user_input.lower())

# output

if result != "":
    print("\nMeaning: \n")
    print("\n\n".join(result))
    print("\n")
else: 
    print("\n\nWord does not exits! Please double check it\n")