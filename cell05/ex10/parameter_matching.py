#!/usr/bin/env python3

import sys

parameters = sys.argv
if len(parameters) == 2:
    text = input("What was the parameter? ")
    if parameters[1] == text:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")