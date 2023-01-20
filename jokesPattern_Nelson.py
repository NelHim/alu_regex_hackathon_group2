#!/usr/bin/python3

import re

joke_pattern = re.compile(r'^Why did the (.*)\? Because (.*)$')

match = joke_pattern.search("Why did the banana go to the doctor? Because it wasn't peeling well.")

if match:
    print(match.group(1)) # banana go to the doctor
    print(match.group(2)) # it wasn't peeling well
else:
    print("Invalid pattern")
