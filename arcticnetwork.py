import sys
import math

parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find_root(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find_root(parent[vertice])
    return parent[vertice]

def union(v1, v2):
    root1 = find_root(v1)
    root2 = find_root(v2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1
            
num_tests = int(sys.stdin.readline())

while (num_tests > 0):
    S, P = map(int, sys.stdin.readline().split(' '))
    pts = []
    
    i = P
    vertices = []
    while (i > 0):
        vertices.append(i)
        make_set(i)
        x, y = map(int, sys.stdin.readline().split(' '))
        pts.append((i,x,y))
        i -= 1
    
    #print(pts)
    edges = [(round(math.hypot(b[1]-a[1], b[2]-a[2]),2), b[0], a[0])
              for a in pts 
              for b in pts[pts.index(a)+1:]]
              
    # Kruskal's:
    edges.sort()
    #print(edges)
    msf = []
    
    for edge in edges:
        if len(msf)==P-1:
            break
        length, v1, v2 = edge
        if find_root(v1) != find_root(v2):
            union(v1, v2)
            msf.append(edge)
    
    #print(vertices)
    #print(edges)
    #print(msf)
    
    # Print msf's longest edge, excluding the longest S-1 edges:
    # (This accounts for the satellite channels)
    print("%.2f" % msf[P-S-1][0])
    num_tests -= 1