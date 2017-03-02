import sys

T = int(sys.stdin.readline())
    
while T>0:
    sys.stdin.readline()
    N = int(sys.stdin.readline())
    i = N
    total_candies = 0
    
    while i>0:
        total_candies += int(sys.stdin.readline())
        i -= 1
        
    if total_candies % N == 0:
        print('YES')
    else:
        print('NO')
    
    T -= 1