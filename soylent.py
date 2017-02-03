import sys

numCases = int(sys.stdin.readline())

while (numCases > 0):
    calories = int(sys.stdin.readline())
    add = 0 if calories % 400 == 0 else 1
    partialBottles = calories // 400
    totalBottles = partialBottles + add
    print(totalBottles)
    numCases -= 1
