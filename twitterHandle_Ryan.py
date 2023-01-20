#!/usr/bin/python3


import re # importing the python regular expression module

# The string to search for matches
string = "Check out my profile @username"

# Search for a match in the string using the re.search() function
# The first argument of the function is the regular expression pattern to search for
# The second argument is the string to search in
match = re.search(r"@([A-Za-z0-9]+)", string)

# Check if a match was found
if match:
    # Extract the matched group using the group() method
    username = match.group(1)

    # Print the extracted value of the twitter handle
    print(f"Twitter handle: @{username}")
else:
    # If no match was found, print a message
    print("No match found.")
