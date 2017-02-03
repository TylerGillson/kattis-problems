import sys

input = sys.stdin.readline()

output = 1

for letter in input:
    if (letter == 'A'):
        if (output == 1):
            output = 2
        elif (output == 2):
            output = 1
    if (letter == 'B'):
        if (output == 2):
            output = 3
        elif (output == 3):
            output = 2
    if (letter == 'C'):
        if (output == 1):
            output = 3
        elif (output == 3):
            output = 1

print(output)