## Sublexical Toolkit Input Prep

This repository contains code and files for updating inputs to the Sublexical Toolkit by utilizing words from the CMU Dictionary. Words are filtered to omit unusable entries (i.e. words such as "AAA" or "'QUOTE", or even phrases). Based on the mappings given by `transcriptions.csv`, all possible IPA transcriptions of the pronunciations from the CMU dictionary are constructed. Such transcriptions are then checked against the Cambridge dictionary for correctness. Discrepancies are identified.

Primary functionality is contained in and described by `inputprep.ipynb`.

### Key Files

`inputprep.ipynb`: contains the key functionality of the word prep. Trims the CMU dictionary, converts pronunciations to their potential IPA formats and compares and contrasts these potential pronunciations with pronunciations obtained from the Cambridge dictionary.

`cmu_ipa_cambridge`: the main, key result. Contains three columns: a word from the cmu dictionary, its corresponding first matching pronunciation from all possible pronunciations for the word as given by the Cambridge dictionary in IPA format (if there is one, and if not ""), and the number of said matching pronunciation (1 if it correpsonds to the first pronunciation from Cambridge, and 2 onward). The final entry is 0 if there is not a corresponding Cambridge pronunciation, and this indicates that there exists a discrepancy between all possible IPA transcriptions from the CMU pronunciation for that word and all pronunciations from the Cambridge dictionary. Take for instance the following examples:

For the word "absorbent", the following is a list of possible IPA transcriptions from the CMU pronunciation: ['əbzɔɹbənt']

The following is a list of pronunciations for "absorbent" from the Cambridge dictionary: ['əbzɔɹbənt', 'əbzɔɹbənt', 'æb', 'sɔɹ']

Thus, the entry in `cmu_ipa_cambridge.csv` is {'Word': 'absorbent', 'IPA Pronunciation': 'əbzɔɹbənt', 'Cambridge Pronunciation Number': 1}

However, for the word "accepting" we have the following:

CMU IPAs: ['æksɛptɪŋ']

Cambridge Pronunciations: ['əksɛptɪŋ']

Clearly, there is a discrepancy here between the two that must be resolved manually, and thus the entry is:

{'Word': 'accepting', 'IPA Pronunciation': '', 'Cambridge Pronunciation Number': 0}

I've been able to reduce the number of discrepancies to 5546 by inspection and some other transcriptions; I think the rest may need to be examined manually, though. A lot of times, it is either because the Cambridge dictionary, when searching for a plural, -ing, etc. only returns the root word. For instance, see the output for the word "titles:"

CMU: ['taɪtəlz']
Cambridge: ['taɪtəl']

`get-cambridge.ipynb`: details the process for obtaining all pronunciations from the Cambridge dictionary. The outputs of this file have already been produced, so it does not need to be run again (and takes several hours to complete if so).

`cambridge_ipas.csv`: the primary output of `get-cambridge.ipynb`. Contains, for all words present in both the trimmed CMU dictionary list and the Cambridge dictionary, words and their potential pronunciations as given by the Cambridge dictionary. If multiple pronunciations are possible, they are space-separated in the second column.

`missing_cmu_words.csv`: contains all words in the trimmed CMU dictionary list whose pronunciations could not be obtained from the Cambridge dictionary. Also contains all possible IPA transcriptions of such words' pronunciations.

### Current Functionality

- Initial filtration of CMU dictionary words
- Generation of all possible transcriptions into IPA of CMU dictionary pronunciations
- Obtains all corresponding pronunciations from Cambridge dictionary in US_IPA format and consolidates them
- Obtains a list of words not present in the Cambridge dictionary from the trimmed CMU list and outputs them 
- Pariwise compares words from the final CMU dictionary and the Cambridge pronunciations to check for discrepancies

### Acknowledgements

[CMU Dictionary](https://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b)

[SUBTLEXUS](https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexus) (used 74,286 word Excel file, which was converted to a csv)

Cambridge Dictionary parser courtesy of [Blackdeer1524](https://github.com/Blackdeer1524/CambridgeDict.py)
