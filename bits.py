import sys

tests = int(sys.stdin.readline())
for i in range(tests):
    ones = []
    number = sys.stdin.readline().strip()
    num = ''
    for n in number:
        num += n
        oneCount = bin(int(num)).count('1')
        ones.append(oneCount)
    print(max(ones))