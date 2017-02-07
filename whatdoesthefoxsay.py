import sys

tests = int(sys.stdin.readline())

for i in range(tests):
    recording = sys.stdin.readline().strip().split(' ')
    ans = ''
    sounds = []
    
    while(True):    
        line = sys.stdin.readline().strip()
        if line == 'what does the fox say?':
            ref = dict(sounds)
            for word in recording:
                if word not in ref:
                    ans = ans + word + ' '
            ans.strip()
            print(ans)
            break
        else:
            data = line.split(' ')
            sounds.append((data[2],data[0]))