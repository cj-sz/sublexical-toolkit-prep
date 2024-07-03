## Sublexical Toolkit Input Prep

This repository contains code and files for updating inputs to the Sublexical Toolkit based on the CMU Dictionary. Words are filtered to omit unusable entries (i.e. words such as "AAA" or "'QUOTE", or phrases). Based on the mappings provided in `transcriptions.csv`, all possible IPA transcriptions of the pronunciations from the CMU dictionary are constructed. Such transcriptions are then checked against the Cambridge dictionary for correctness.

Primary functionality is contained in and described by `inputprep.ipynb`.

### Key Result

`cmu_ipa_cambridge.csv`

*CMU Word*: A word from the trimmed list of CMU words. Some of these will be junk (like "aa", for instance) and will need to be filtered out by hand as they are examined. If a word appears twice in this column (and therefore has two separate entries), that means the CMU dictionary provided more than one valid pronunciation for the word.

*CMU IPAs*: A list of all possible IPA transcriptions of the pronunciation for the word provided by the CMU dictionary. Note that these are NOT alternate pronunciations; sometimes, there is more than one way to represent a phoneme in the IPA format (see `transcriptions.csv`), and this list includes all valid combinations of such representations. Again, if there is a valid alternate pronunciation for a word, that pronunciation would show up in a separate row entry for the word.

*Cambridge IPAs*: A list, possibly empty, of all IPA pronunciations for the given word returned by the Cambridge dictionary (if any).

*CMU (Toolkit)*: A list of all pronunciations in *CMU IPAs* translated to the Toolkit pronunciation format. Trimmed to remove duplicates.

*Cambridge (Toolkit)*: A list of all pronunciations in *Cambridge IPAs* translated to the Toolkit pronunciation format. Trimmed to remove duplicates, and empty if *Cambridge IPAs* is empty for this word.

*Matched Pronunciations (IPA)*: A list, possibly empty, of all matched IPA pronunciations from the *CMU IPAs* list and the *Cambridge IPAs* list. 

*Matched Pronunciations (Toolkit)*: A list of all pronunciations in *Matched Pronunciations (IPA)* translated to Toolkit format. Trimmed to remove duplicates, and empty if *Matched Pronunciations (IPA)* is empty.

*Pronunciation Matches*: A list of tuples indicating which (if any) CMU IPA from *CMU IPAs* matched which Cambridge IPA from *Cambridge IPAs* in the format of "(cmu_ipa_number, matched_cambridge_ipa_number)".

*Alternate Pronunciation*: 1 if this is a word that had other valid pronunciations present in the CMU dictionary. 0 otherwise.

*Root From Cambridge*: Sometimes, querying the Cambridge dictionary for the conjugate of a word only returns information on the root of the word. For instance, see the word "abandoning" on line 17; the entries in *Cambridge IPAs* correspond to the pronunciation of the word "abandon," rather than "abandoning." This column will be 1 if this was the case, and 0 otherwise; this occurred 15,960 times.

*Missing From Cambridge*: 1 if the word wasn't present at all in the Cambridge dictionary (meaning nothing at all was returned from the query). This was true for 8,248 words.

*Top Pronunciation (ALL)*: 1 if this row corresponds to the top pronunciation for a word (i.e. was the first pronunciation provided for the word in the CMU dictionary), REGARDLESS of whether or not the word had alternate valid pronunciations present in the dictionary. For example, this row is 1 for the first pronunciation provided for "record" to indicate it is the top pronunciation for record (see line 38,616), and is ALSO 1 for "abandon" on line 15, which is only present once.

This can be used for filtering if we, say, want to include only the top pronunciation for all words that do have valid alternate pronunciations, plus words that don't (i.e. words that only appeared once in the CMU dictionary) as a possible filter to obtain only one entry per word (and include all words).

*Top Pronunciation (ALT ONLY)*: 1 if this row corresponds to the top pronunciation for a word that does have other valid alternate pronunciations; an example where this would be the case is the first pronunciation provided for the word "record" (see line 38,616); notice that it is 0 for the two subsequent pronunciations provided (indicating that they were not the top pronunciation for the word). Since this column is only for words with alternate pronunciations present, it is also 0 for words that only appear once, like "abandon."

### Acknowledgements

[CMU Dictionary](https://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b)

[SUBTLEXUS](https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexus) (used 74,286 word Excel file, which was converted to a csv)

Cambridge Dictionary parser from [Blackdeer1524](https://github.com/Blackdeer1524/CambridgeDict.py)
