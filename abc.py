import sys

x, y, z = [int(i) for i in sys.stdin.readline().strip().split()]
a, b, c = [i for i in sys.stdin.readline().strip()]

nums = [x,y,z]
nums.sort()
origOrder = [a, b, c]
order = [a, b, c]
order.sort()

key = dict(zip(order, nums))

output = ''
for i in origOrder:
    output = output + str(key[i]) + ' '

output.strip()
print(output)