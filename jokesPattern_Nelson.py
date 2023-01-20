#!/usr/bin/python3
import re

movie_title_pattern = re.compile(r'^(.*)\s\((\d{4})\)$')
match = movie_title_pattern.search("Avatar The way of water (2022)")

if match:
    print(match.group(1)) # Avatar The way of water
    print(match.group(2)) # 2022
else:
    print("Invalid pattern")
