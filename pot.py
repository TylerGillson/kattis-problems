import sys
import math

N = int(sys.stdin.readline())
total = 0

while N>0:
    data = sys.stdin.readline().strip()
    base = int(data[:len(data)-1:])
    power = int(data[-1])
    num = int(math.pow(base,power))
    total = total + num
    N -= 1

print(total)