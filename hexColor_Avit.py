#!/usr/bin/python3
import re


string = "API data"

pattern = re.compile(r"#[a-fA-F\d]{6}")


matches = pattern.finditer(string)


for match in matches:
    print(match.group())

