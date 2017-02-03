#! /usr/bin/env python3

import sys

num_lines = int(sys.stdin.readline())
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while(num_lines > 0):
    flag = True
    missing = []
    line = sys.stdin.readline().lower().rstrip()
    line = list(line)
        
    for letter in alpha:
        if (letter in line) == False:
            flag = False
            missing.append(letter)
    
    if flag == True:
        print('pangram')
    else:
        missing_str = ''
        for letter in missing:
            missing_str = missing_str + letter
        print('missing', missing_str)
            
    num_lines -= 1