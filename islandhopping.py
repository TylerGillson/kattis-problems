import sys
import heapq
import math

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = 99999999999999
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None
    def __lt__(self, other):
        return (self.distance < other.distance)
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
    def get_connections(self):
        return self.adjacent.keys()  
    def get_id(self):
        return self.id
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
    def set_distance(self, dist):
        self.distance = dist
    def get_distance(self):
        return self.distance
    def set_previous(self, prev):
        self.previous = prev
    def set_visited(self):
        self.visited = True
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
    def __iter__(self):
        return iter(self.vert_dict.values())
    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex
    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None
    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)
    def get_vertices(self):
        return self.vert_dict.keys()
    def set_previous(self, current):
        self.previous = current
    def get_previous(self, current):
        return self.previous

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

def dijkstra(aGraph, start):
    length = 0.0
    # Set the distance for the start node to zero 
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                length += next.get_distance()
                #print 'updated : current = %s next = %s new_dist = %s' \
                #        %(current.get_id(), next.get_id(), next.get_distance())
            #else:
            #    print 'not updated : current = %s next = %s new_dist = %s' \
            #            %(current.get_id(), next.get_id(), next.get_distance())

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)
    return length

N = int(sys.stdin.readline())
g = Graph()

while (N > 0):
    M = int(sys.stdin.readline())
    i = M
    output = 0.0
    pts = []
    
    while (i > 0):
        g.add_vertex(i)
        x, y = map(float, sys.stdin.readline().split(' '))
        pts.append((i,x,y))
        i -= 1
    #print(pts)
    
    edges = [(round(math.hypot(b[1]-a[1], b[2]-a[2]),2), b[0], a[0])
              for a in pts 
              for b in pts[pts.index(a)+1:]]
          
    for edge in edges:
        g.add_edge(edge[1],edge[2],edge[0])
        
    print("%.3f" % dijkstra(g, g.get_vertex(M)))
    N -= 1