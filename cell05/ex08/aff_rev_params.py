import sys

parameters = sys.argv
if len(parameters) <= 2:
    print("none")
else:
    print(*[x for x in reversed(parameters[1:])], sep='\n')