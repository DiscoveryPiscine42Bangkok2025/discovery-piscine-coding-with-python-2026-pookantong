#!/usr/bin/env python3

import sys

parameters = sys.argv
if len(parameters) > 2:
    for text in parameters[1:]:
        if not text.endswith("ism"):
            print(text+"ism")
else:
    print("none")