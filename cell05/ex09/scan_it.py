#!/usr/bin/env python3

import sys

parameters = sys.argv
if len(parameters) == 3:
    print(parameters[2].count(parameters[1]))
else:
    print("none")