import sys

hour, minutes = map(int, sys.stdin.readline().split())
if minutes - 45 > 0:
    print(hour, minutes - 45)
else:
    if hour == 0:
        print(23,60-((minutes-45)*-1))
    else:
        print(hour - 1,60-((minutes-45)*-1))