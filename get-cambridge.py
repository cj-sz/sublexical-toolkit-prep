# This file generates a csv of English words and their IPA pronunciations
# as given in the Cambridge Dictionary. Uses the same filtration criteria
# as inputprep.
#
# This script is incomplete
import cambridge_parser as parser
import pandas as pd
import re

# Empty dict to contain words and pronunciations to be turned into csv later
wps = {} # str : List[str]

with open('cmudict-0.7b-2024-4-6.txt') as file:
    print("Trimming cmu dict...")
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

    l = 56

    # Skip the first 56 lines as these contain text we are not interested in
    for line in file.readlines()[56:]:
        print(f"Reading line {l} of cmu dict...",end="\r")


        s = line.strip()
        i = s.find(" ", 0)
        word = s[:i].lower()
        word = word.lower()

        # Ensure the word doesn't contain punctuation and is present in the SUBTLEXUS
        if re.match(rpunc, word) is None \
            and re.match(rpeat, word) is None \
            and word in subtlexus['Word'].values:
            # Add the word to the dict 
            wps[word] = []

        l += 1

print("")
print("Finished trimming cmu dict.")
print("Obtaining Cambridge pronunciations...")

# For each word in the dict, get its corresponding pronunciation from Cambridge;
# if it is not in Cambridge, remove it from the dict 

# list of words to eventually remove
to_remove = []

i = 1
wps_words = str(len(wps.keys()))

# Iterate through trimmed word list 
for word in wps.keys():
    print(f"Obtaining pronunciations for word {word}; {i} of {wps_words} words...", end="\r")

    # Grab cambridge information
    cword = parser.define(word)

    # List of pronunciations for the word in US_IPA
    ps = []

    # Iterate through all definitions
    for defnum in range(len(cword)):
        try:
            # Obtain all pronunciations and format them correctly
            pslist = cword[defnum][word][0]['data']['US_IPA']
            for p in pslist:
                # Append the formatted pronunciation to list of pronuns
                ps.append(p[0].replace(".","").replace("/",""))
        except (RuntimeError, KeyError, IndexError):
            # Continue iterating if no pronunciation present
            continue 

    # If there are no pronunciations for the word, add the word to a list
    # of words to be removed
    if len(ps) == 0:
        to_remove.append(word)
    else:
        wps[word] = ps

    i += 1

print("")
print("Finished obtaining pronunciations.")

# Remove all words with no pronunciations
for word in to_remove:
    wps.pop(word)

print("Removed all words without pronunciations.")

# Output to csv
df = pd.DataFrame.from_dict(wps)
df.to_csv("cambridge_ipas.csv", index=False)

print("Output csv to cambridge_ipas.csv")
