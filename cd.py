#! /usr/bin/env python3

import sys

numCds = sys.stdin.readline()
jack = int(numCds.split(' ')[0])
jill = int(numCds.split(' ')[1])

jackList = []
jillList = []

i = 0
while (i < jack):
    jackList.append(int(sys.stdin.readline()))
    i += 1
    
i = 0
while (i < jill):
    jillList.append(int(sys.stdin.readline()))
    i += 1
    
sell = 0
ni = 0
mi = 0

while (ni < jack and mi < jill):
    if jackList[ni] > jillList[mi]:
        mi += 1
    elif jackList[ni] < jillList[mi]:
        ni += 1
    else:
        sell += 1
        ni += 1
        mi += 1

print(sell)