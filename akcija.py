import sys

N = int(sys.stdin.readline())
prices = []

while N>0:
    p = int(sys.stdin.readline())
    prices.append(p)
    N -= 1

prices = sorted(prices, reverse=True)
lowest_price = 0
i = 1

for p in prices:
    if i % 3 == 0:
        i += 1
        continue
    i += 1
    lowest_price += p

print(lowest_price)
