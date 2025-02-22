#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
import sys
import re
from spellchecker import SpellChecker

spell = SpellChecker()

for line in sys.stdin:
    words = re.findall(r'\w+', line.lower())  # Extract words, convert to lowercase
    for word in words:
        if word not in spell:  # If word is NOT in English dictionary
            print(f"{word}\t1")  # Emit word and count

