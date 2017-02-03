import sys
import math

for line in sys.stdin.readlines():
    num = int(line)
    status = ''
    
    divisors = [1]
    for i in range(2,math.floor(math.sqrt(num))+1):
        if num % i == 0:
            divisors.append(i)
            if i != num/i:
                divisors.append(num/i)
        
    total = sum(divisors)
    if total == num:
        status = 'perfect'
    elif total in range(num-2,num+3):
        status = 'almost perfect'
    else:
        status = 'not perfect'
    
    print(num,status)