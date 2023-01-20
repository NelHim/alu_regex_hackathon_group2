#!/usr/bin/python3


import re

# The string to search for matches
string = "[Verse 1] Some lyrics here"

# Compile the regular expression pattern
pattern = re.compile(r"\[Verse (\d+)\] (.+)")

# Search for a match in the string
match = pattern.search(string)

# Check if a match was found
if match:
    # Extract the matched groups
    verse = match.group(1)
    lyrics = match.group(2)

    # Print the extracted values
    print(f"Verse: {verse}\nLyrics: {lyrics}")
else:
    print("No match found.")
