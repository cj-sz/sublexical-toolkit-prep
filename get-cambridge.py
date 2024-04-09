# This file generates a csv of English words and their IPA pronunciations
# as given in the Cambridge Dictionary. Uses the same filtration criteria
# as inputprep.
#
# This script is incomplete
import cambridge_parser as parser
import pandas as pd
import re

# Initialize an empty DataFrame
df = pd.DataFrame(columns=['Word', 'Pronunciation'])

with open('cmudict-0.7b-2024-4-6.txt') as file:
    # Import the SUBTLEXUS csv to a pandas dataframe.
    subtlexus = pd.read_csv('SUBTLEXusExcel2007.csv')

    # Convert all words to lowercase
    subtlexus['Word'] = subtlexus['Word'].str.lower()

    # Regex for finding unwanted punctuation in words (essentially any non-word)
    rpunc = r".*(\W|\d).*"

    # Regex for three-peated characters (any word with three or more of the same
    # letter in a row should be omitted, as none are valid English words for the
    # purposes of the toolkit)
    rpeat = r".*(.)\1\1.*"

    # Skip the first 56 lines as these contain text we are not interested in
    for line in file.readlines()[56:]:
        s = line.strip()
        i = s.find(" ", 0)
        word = s[:i].lower()
        word = word.lower()
        # Ensure the word doesn't contain punctuation and is present in the SUBTLEXUS
        if re.match(rpunc, word) is None \
            and re.match(rpeat, word) is None \
            and word in subtlexus['Word'].values:
            # Append a row to the DataFrame
            df = pd.concat([df, pd.DataFrame({'Word': [word], 'Pronunciation': ['']})], ignore_index=True)


print(df[:5])
