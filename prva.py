import sys

data = sys.stdin.readline()
rows = int(data.split(' ')[0])
columns = int(data.split(' ')[1])
words = []
vwords = ['' for x in range(columns)]

# Extract Horizontal Words:
while (rows > 0):
    row = sys.stdin.readline().strip()
    chunks = row.split('#')
    if '' in chunks:
        chunks.remove('')
    for word in chunks:
        words.append(word)
    
    # Extract Vertical Strings:
    index = 0
    for letter in row:
        vwords[index] = vwords[index] + letter
        index += 1
    
    rows -= 1
    
# Extract Vertical Words:
for vword in vwords:
    chunks = vword.split('#')
    if '' in chunks:
        chunks.remove('')
    for word in chunks:
        words.append(word)

# De-dupe and sort lexicographically:
words = set(words)
words = [x for x in words if len(x) > 1]
words = list(words)
words.sort()

# Return Output:
print(words[0])