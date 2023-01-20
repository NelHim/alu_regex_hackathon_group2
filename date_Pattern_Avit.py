#!/usr/bin/python3
import re


string = "API data"

date_pattern = r"(\d{2})-([A-Za-z]{3})-(\d{4})"

matches = re.findall(date_pattern, string)


for match in matches:
    print(match)

