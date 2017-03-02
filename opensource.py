import sys
from operator import itemgetter
from collections import Counter

summary = {}
all_users = []
    
def print_summary(summary):
    s = sorted(summary.items(), key=itemgetter(0))
    for key, value in sorted(s, key=itemgetter(1), reverse=True):
        print(key,value)
    
def de_dupe(summary,all_users):
    count = Counter(i[1] for i in all_users)
    dupes = [i for i in all_users if count[i[1]] > 1]
    
    for dupe in dupes:
        summary[dupe[0]] -= 1
    
while True:
    line = sys.stdin.readline().strip()
    
    if line == '1':
        de_dupe(summary,all_users)
        print_summary(summary)
        summary = {}
        all_users = []
        continue
    
    if line == '0':
        break
    
    if line.isupper():
        users = []
        summary[line] = 0
        project = line
    else:
        if line in users:
            continue
        else:
            users.append(line)
            all_users.append((project,line))
            summary[project] += 1