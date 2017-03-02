import sys

output = ''

while True:
    num_lines = int(sys.stdin.readline())
    if num_lines == 0:
        output = output[0:-2:]
        break
    length = 0
    error = False
    old_length = 0
    
    for i in range(num_lines):
        line = sys.stdin.readline().strip().split()
        char = line[0]
        for reps in line[1:]:
            reps = int(reps)
            output = output + char*reps
            length += reps
            if char == '#':
                char = '.'
            else:
                char = '#'
        output = output + '\n'
        if i == 0:
            old_length = length
        if length != old_length:
            error = True
        old_length = length
        length = 0
    
    if error == True:
        output = output + 'Error decoding image\n'
    output = output + '\n'

print(output)