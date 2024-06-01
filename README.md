## Sublexical Toolkit Input Prep

This repository contains code and files for updating inputs to the Sublexical Toolkit based on the CMU Dictionary. Words are filtered to omit unusable entries (i.e. words such as "AAA" or "'QUOTE", or phrases). Based on the mappings provided in `transcriptions.csv`, all possible IPA transcriptions of the pronunciations from the CMU dictionary are constructed. Such transcriptions are then checked against the Cambridge dictionary for correctness.

Primary functionality is contained in and described by `inputprep.ipynb`.

### Key Files

`inputprep.ipynb`: contains the key functionality of the word prep. Trims the CMU dictionary, converts pronunciations to their potential IPA formats and compares and contrasts these potential pronunciations with pronunciations obtained from the Cambridge dictionary. Outputs `cmu_ipa_cambridge.csv`, the main result of the analysis (described below).

`cmu_ipa_cambridge.csv`: the main, key result. Contains the following columns:

*CMU Word*: a word from the trimmed CMU dictionary. Duplicates can exist (see *Alternate Pronunciation*)

*CMU IPAs*: a list of strings containing all possible IPA transcriptions of the pronunciation provided for the word by the CMU dictionary.

*Cambridge IPAs*: a list, possibly empty, of pronunciations returned for the word through a query to the Cambridge dictionary. If the list is empty, the word was missing from the Cambridge dictionary. Existing pronunciations are provided in IPA format.

*Matched Pronunciations (IPA)*: a possibly empty list of all possible pronunciations returned both by the CMU dictionary transcription and the Cambridge dictionary. Indicates the pronunciations where the two dictionaries agree.

*Matched Pronunciations (Toolkit)*: a list not necessarily the same length as the list in *Matched Pronunciations (IPA)* consisting of all such matched pronunciations converted to the format used as input in the Sublexical Toolkit, and trimmed to remove duplicates.

*Pronunciation Matches*: a listof one-indexed pairs indicating the indices of the matched pronunciations. For instance, if two matched pronunciations were found, and one was the first pronunciation of the CMU dictionary matched with the second of the Cambridge, and the second match was the second pronunciation of the CMU dictionary matched with the third of Cambridge, this list would be [(1,2), (2, 3)]. This list is not necessarily the same length as *Matched Pronunciations (Toolkit)* but is guaranteed to be the same length as *Matched Pronunciations (IPA)*.

*Alternate Pronunciation*: An integer. 1 if the word is present for at least the second time in the CMU dictionary. If it is, this means the CMU dictionary identified more than one valid pronunciation for the word, and the word appears more than once in the *CMU Word* column.

*Root From Cambridge*: An integer. Sometimes, when querying the conjugation of a word (often this happens for part of speech or tense), Cambridge returns the root of the word (as an example see the entry for the word "abandoning" in `cmu_ipa_cambridge.csv`). In this case, the provided pronunciations are the pronunciations for the root word. None of the pronunciations will match the CMU dictionary pronunciation, and before input to the Toolkit these will need to be examined manually. The entry for this column is 1 if this is the case and 0 otherwise.

*Missing From Cambridge*: An integer. 1 if the word was missing from the Cambridge dictionary, and 0 otherwise.

`get-cambridge.ipynb`: details the process for obtaining all pronunciations from the Cambridge dictionary. The outputs of this file have already been produced, so it does not need to be run again (and takes several hours to complete if so).

`cambridge_ipas.csv`: the primary output of `get-cambridge.ipynb`. Contains, for all words present in both the trimmed CMU dictionary list and the Cambridge dictionary, words and their potential pronunciations as given by the Cambridge dictionary. If multiple pronunciations are possible, they are space-separated.

### Acknowledgements

[CMU Dictionary](https://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b)

[SUBTLEXUS](https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexus) (used 74,286 word Excel file, which was converted to a csv)

Cambridge Dictionary parser courtesy of [Blackdeer1524](https://github.com/Blackdeer1524/CambridgeDict.py)
