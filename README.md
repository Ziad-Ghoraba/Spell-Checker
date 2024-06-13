# Spell-Checker
Overview
This project is a simple spell checker implemented in Python. It uses a binary search algorithm to check if words exist in a given dictionary and suggests corrections for misspelled words using sequence matching.

Features
Word Existence Check: Uses binary search to efficiently check if a word exists in the dictionary.
Spelling Suggestions: Provides up to three word suggestions for misspelled words using the difflib library.
Red Underline for Errors: Highlights misspelled words with a red underline for easy identification.
Installation
To run this project, you need to have Python installed on your machine. Additionally, ensure you have the difflib module, which is part of the standard Python library.

Usage
Prepare the Dictionary:

Place your dictionary file (Project_Dictionary.txt) in the specified path (D:\\Programming\\Projects\\Data\\Spell_Checker\\).
Run the Spell Checker:

Execute the Spell_Checker.py script.
The script reads the dictionary file, processes the input text, checks for spelling errors, and provides suggestions for misspelled words.
Functions
binary_search(word_list, item)
Performs a binary search to determine if item exists in word_list.

check_word(word)
Removes non-alphabetic characters from word and checks if the cleaned word exists in the dictionary.

red_line(word)
Returns the word with a red underline for terminal display.

matches(word, n)
Uses difflib.SequenceMatcher to find and return up to n suggestions for word from the dictionary.

Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss what you would like to change.
