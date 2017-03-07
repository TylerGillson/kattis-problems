import sys

votes = {}

while True:
    line = sys.stdin.readline().strip()
    if line == '***':
        break
    if line in votes:
        votes[line] += 1
    else:
        votes[line] = 1
    
maj = ('',0)
for candidate, score in votes.items():
    if score > maj[1]: 
        tie = False
        maj = candidate, score
    elif score == maj[1]:
        tie = True

if tie == True:
    print('Runoff!')
else:
    print(maj[0])