## Sublexical Toolkit Input Prep

This repository contains code and files for updating inputs to the Sublexical Toolkit by utilizing words from the CMU Dictionary. Words are filtered to omit unusable entries (i.e. words such as "AAA" or "'QUOTE", or even phrases). Based on the mappings given by `transcriptions.csv`, all possible IPA transcriptions of the pronunciations from the CMU dictionary are constructed. Such transcriptions are then checked against the Cambridge dictionary for correctness. Discrepancies are identified.

Primary functionality is contained in and described by `inputprep.ipynb`.

### Current Functionality

- Initial filtration of CMU dictionary words
- Generation of all possible transcriptions into IPA of CMU dictionary pronunciations

### Acknowledgements

[CMU Dictionary](https://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict-0.7b) used
[SUBTLEXUS](https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexus) (used 74,286 word Excel file, which was converted to a csv)
Cambridge Dictionary parser courtesy of [Blackdeer1524](https://github.com/Blackdeer1524/CambridgeDict.py)
