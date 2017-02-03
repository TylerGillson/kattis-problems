import sys

num = int(sys.stdin.readline())
minions = []
for i in range(num):
	min, max = map(int, sys.stdin.readline().split(' '))
	minions.append((min, max))

minions = sorted(minions)
rooms = 1


print(minions)

grouping = False
loner = False

for i in range(num-1):
    if i == num-1:
        if grouping == False:
            rooms += 1
    else:
        if minions[i][1] < minions[i+1][0]:
            loner = True
            rooms += 1
        elif minions[i][1] >= minions[i+1][0] and minions[i][1] < minions[i+2][0]:
            grouping = False
        elif minions[i][1] >= minions[i+1][0] and minions[i][1] >= minions[i+2][0]:
            grouping = True
    
        if loner == False and grouping == False:
            rooms += 1
    
print(rooms)