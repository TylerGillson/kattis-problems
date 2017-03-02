import sys

john = sys.stdin.readline()
doc = sys.stdin.readline()

if len(john) >= len(doc):
    print('go')
else:
    print('no')