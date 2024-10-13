import pandas

phonetics = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetics_data_frame = pandas.DataFrame(phonetics)


#TODO 1. Create a dictionary in this format:
code_dictionary = {row.letter:row.code for (index, row) in phonetics_data_frame.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word\n")
result = [code_dictionary[letter.upper()] for letter in user_word]

print(result)