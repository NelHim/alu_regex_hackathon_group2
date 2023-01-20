#!/usr/bin/python3


import re # importing the python regular expression module

# The string to search for matches
string = "The IP address is 192.168.1.1"

# Search for a match in the string using the re.search() function
# The first argument of the function is the regular expression pattern to search for
# The second argument is the string to search in
match = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", string)

# Check if a match was found
if match:
    # Extract the matched group using the group() method
    # The first group is the IP address
    ip_address = match.group(1)

    # Print the extracted value of the IP address
    print(f"IP address: {ip_address}")
else:
    # If no match was found, print a message
    print("No match found.")
