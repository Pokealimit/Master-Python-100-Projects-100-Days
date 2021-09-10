student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

import pandas
# Read CSV
df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(df)

# Create dictionary from dataframe
alphabet_list = {row.letter:row.code for (index, row) in df.iterrows()}
# print(alphabet_list)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    
    word = input("Enter a word: ")
    # Don't have to convert to a list of letters as "for letter in word" will automatically convert to list of letters
    # letters = list(word)
    try:
        phonetic_code_word = [alphabet_list[letter] for letter in word.upper()]
        print(phonetic_code_word)
    except KeyError:
        print("Sorry, only letters in the alphabet please.")