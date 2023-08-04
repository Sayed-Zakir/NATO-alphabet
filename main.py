import pandas as pd

data= pd.read_csv("nato_phonetic_alphabet.csv")

data_dict={row.letter:row.code for (index, row) in data.iterrows()}

user_name=input("What is your name? ").upper()

output=[data_dict[letter] for letter in user_name]

print(output)
