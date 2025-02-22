#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
import sys
from collections import defaultdict

word_counts = defaultdict(int)

for line in sys.stdin:
    try:
        word, count = line.strip().split("\t")
        word_counts[word] += int(count)
    except ValueError:
        continue  # Skip malformed lines

for word, count in word_counts.items():
    print(f"{word}\t{count}")


