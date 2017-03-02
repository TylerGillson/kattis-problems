import sys
import math
#import itertools

#def tight(tup):
#    if len(tup) == 1:
#        return True
#    if abs(tup[0]-tup[1]) > 1:
#        return False
#    tup = tup[1:]
#    return tight(tup)

def nums(i, j, k):
    if (i < 0 or j < 0 or j > k):
        return 0
    if (i == 1):
        return 1
    
    m[i][j] = nums(i-1, j, k) + nums(i-1, j-1, k) + nums(i-1, j+1, k)
    return m[i][j]
    
for line in sys.stdin.readlines():
    K, N = map(int, line.split(' '))
    
#    lang = [x for x in range(K+1)]
#    words = [p for p in itertools.product(lang, repeat=N) if tight(p)]
    sum = 0
    for i in range(K+1):
        m = [[0] * 10 for i in range(101)]
        sum += nums(N, i, K)
        print(m)
    output = sum/math.pow(K+1,N)*100
#    output = len(words)/math.pow(K+1,N)*100
    print('%.7f' % output)