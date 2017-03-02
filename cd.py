#! /usr/bin/env python3

import sys

while (True):
    jack, jill = map(int, sys.stdin.readline().split(' '))
    if jack==0 and jill==0:
        break
    
    jack_cds = [0]*1000000
    jill_cds = [0]*1000000
    
    for i in range(jack):
        jack_cds[i] = int(sys.stdin.readline())
    for i in range(jill):
        jill_cds[i] = int(sys.stdin.readline())
    
    sell = 0
    jack_i = 0
    jill_i = 0
    
    while (jack_i < jack and jill_i < jill):
        if jack_cds[jack_i] > jill_cds[jill_i]:
            jill_i += 1
        elif jack_cds[jack_i] < jill_cds[jill_i]:
            jack_i += 1
        else:
            sell += 1
            jack_i += 1
            jill_i += 1
            
    print(sell)