import sys

tests = int(sys.stdin.readline())
while tests > 0:
    num = int(sys.stdin.readline())
    if num % 2 == 0:
        print(num,'is even')
    else:
        print(num,'is odd')
    tests -= 1