import sys

morseCodes = ('.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','..--','---.','.-.-','----')
morseVals = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','.',',','?')

for line in sys.stdin.readlines():
    morse = ''
    output = ''
    numbers = ''

    # Iterate through the input line to generate morse & numbers:
    for letter in line:
        index = 0
        for item in morseVals:
            if item == letter:
                morse = morse + morseCodes[index]
                numbers = numbers + str(len(morseCodes[index]))
                break
            else:
                index += 1

    # Reverse the numbers String:
    numbers = numbers[::-1]

    # Convert using reversed numbers string:
    for num in numbers:
        index = 0
        code = morse[:int(num):1]
        morse = morse[int(num)::1]
    
        for item in morseCodes:
            if item == code:
                output = output + morseVals[index]
                break
            else:
                index += 1
    
    print(output)
        
        
        
        
        