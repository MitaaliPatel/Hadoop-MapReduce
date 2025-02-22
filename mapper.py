#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    words = re.findall(r'\w+', line.lower())  # Convert to lowercase & extract words
    for word in words:
        print(f"{word}\t1")  # Emit word and count

