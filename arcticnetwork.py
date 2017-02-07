import sys
import math
from operator import itemgetter

ADD = 0

def creates_cycle(tree, edge):
    for vertice in tree:
        if vertice[1] == edge[1]:
            return True
    return False

num_tests = int(sys.stdin.readline())
while (num_tests > 0):
    S, P = map(int, sys.stdin.readline().split(' '))
    pts = []
    
    i = P
    while (i > 0):
        x, y = map(int, sys.stdin.readline().split(' '))
        pts.append((i,x,y))
        i -= 1
    
    edges = [(b[0],a[0],round(math.hypot(b[1]-a[1], b[2]-a[2]),2))
              for a in pts for b in pts
              if pts.index(b) > pts.index(a)]
    
    # Kruskal's:
    edges = sorted(edges,key=itemgetter(2))
    
    msf = []                # List for minimum spanning forest
    msf.append(edges[0])    # Add the first edge to the forest
    del edges[0]            # Remove it from the list
    
    # Create the msf:
    for edge in edges:
        if len(msf)==(P-1):
            break
        elif creates_cycle(msf,edge) == True:
            continue
        else:
            msf.append(edge)
    
    # Print msf's longest edge, excluding the longest S-1 edges:
    # (This accounts for the satellite channels)
    print(msf[P-S-1][2])
    num_tests -= 1