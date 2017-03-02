import sys

for line in sys.stdin:
    data = line.strip().split(' ')
    C = float(data[0])
    N = int(data[1])
    
    knapsack = [(0,0,0)]*2000
    objects = [(0,0)]*2000
    
    for i in range(N):
        a, b = map(int, sys.stdin.readline().strip().split(' '))
        objects[i] = a, b
    
    for i in range(N):
        knapsack[i][0] = i
        knapsack[i]