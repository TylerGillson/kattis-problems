#! /usr/bin/env python3

import sys

runs = int(sys.stdin.readline())
output = 0

while(runs > 0):
    val = sys.stdin.readline().strip()
    total = 0
    for num in val:
        total += int(num)
    
    if val[len(val)-4:] == '0000':
        output = int(val) - 10000
    if (val[len(val)-3:] == '000') and (val[len(val)-4] != '0'):
        output = int(val) - 1000
    if val[len(val)-2:] == '00' and (val[len(val)-3] != '0'):
        output = int(val) - 100
    if val[len(val)-1] == '0' and (val[len(val)-2] != '0'):
        output = int(val) - 10
    if val[len(val)-1] != '0':
        output = int(val) - 1
    if total == 1:
        output = 0
    
    print(output)
    runs -= 1