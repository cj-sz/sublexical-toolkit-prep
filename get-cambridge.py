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

wps_keys = list(wps.keys())
wps_words = str(len(wps_keys))
# Four steps of iteration to prevent errors
step = int(len(wps_keys) / 4) # TODO turn the step into a variable
stepn = 1
wordnum = 1

# Iterate through trimmed word list 
# This is done in several steps to reduce capacity for errors
for i in range(0, len(wps_keys), step):
    # Temporary dict in which to store words from this iteration
    temp_words = {}
    words_to_remove = []

    # todo dont hardcode 4
    print(f"Stepping through words {wps_keys[i]} to {wps_keys[i+step]} in step {str(stepn)} of 4...")

    for word in wps_keys[i:min(len(wps_keys), i + step)]:
        print(f"Obtaining pronunciations for word {word}; {str(wordnum)} of {wps_words} words...", end="\r")

        # Grab cambridge information
        cword = parser.define(word)

        # List of pronunciations for the word in US_IPA in space-separated string
        ps = ""

        # Iterate through all definitions
        for defnum in range(len(cword)):
            try:
                # Obtain all pronunciations and format them correctly
                pslist = cword[defnum][word][0]['data']['US_IPA']
                for p in pslist:
                    # Append the formatted pronunciation to space separated string of pronuns
                    ps = ps + " " + p[0].replace(".","").replace("/","")
            # if something times out we can grab it later by hand 
            except (RuntimeError, KeyError, IndexError, TimeoutError):
                # Continue iterating if error occurs; these can be cleaned up manually later
                continue 

        # If there are no pronunciations for the word, add the word to a list
        # of words to be removed
        if len(ps) == 0:
            words_to_remove.append(word)
        else:
            temp_words[word] = ps

        wordnum += 1
    # Output the words and pronunciations we have accumulated
    print("")
    print("Finished obtaining pronunciations for this iteration.")
    
    for word in words_to_remove:
        temp_words.pop(word)
    
    print("Removed all words without pronunciations.")

    word_pronunciation_pairs = []

    # Iterate through the dictionary and convert it into a list of tuples
    for word, pronunciation in temp_words.items():
        # Append each word-pronunciation pair as a tuple to the list
        word_pronunciation_pairs.append((word, pronunciation))

    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(word_pronunciation_pairs, columns=['Word', 'Pronunciation'])

    # Output the DataFrame to a CSV file
    df.to_csv(f"cambridge_ipas_step{str(stepn)}.csv", index=False)

    print(f"Output csv for step {str(stepn)} to cambridge_ipas_step{str(stepn)}.csv")
    
    stepn += 1

# Now read all the results back in, concat them and make a big csv with all the
# cambridge ipas
