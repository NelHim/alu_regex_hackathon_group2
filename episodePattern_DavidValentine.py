#!/usr/bin/python3


import re # importing the python regular expression module

# The string to search for matches
string = "The show's name is Game of Thrones S01E01: Winter is Coming"

# Search for a match in the string using the re.search() function
# The first argument of the function is the regular expression pattern to search for
# The second argument is the string to search in
match = re.search(r"(.+) S(\d{2})E(\d{2}): (.+)", string)

# Check if a match was found
if match:
    # Extract the matched groups using the group() method
    # The first group is the show name
    show_name = match.group(1)
    # The second group is the season number
    season = match.group(2)
    # The third group is the episode number
    episode = match.group(3)
    # The fourth group is the episode title
    episode_title = match.group(4)

    # Print the extracted values using the formatted string
    print(f"Show Name: {show_name}\nSeason: {season}\nEpisode: {episode}\nTitle: {episode_title}")
else:
    # If no match was found, print a message
    print("No match found.")
