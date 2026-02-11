#!/usr/bin/env python3

import sys

parameters = sys.argv
if len(parameters) == 2:
    z_count = parameters[1].count("z")
    if z_count > 0:
        print("z"*z_count)
    else:
        print("none")
else:
    print("none")