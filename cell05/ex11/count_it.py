#!/usr/bin/env python3

import sys

parameters = sys.argv
if len(parameters) >= 2:
    print(f"parameters: {len(parameters) - 1}")
    for param in parameters[1:]:
        print(f"{param}: {len(param)}")
else:
    print("none")