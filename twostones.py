import sys

input = int(sys.stdin.readline())

ans = input % 2
if (ans == 0):
    print('Bob')
else:
    print('Alice')