from collections import deque

# n, m = map(int, input().split())

# # constructs an undirected graph G of n vertex amd m edges
# g = {}

# for i in range(1, n + 1):
#     g[i] = set()

# for i in range(m):
#     u, v = map(int, input().split())
#     g[u].add(v)
#     g[v].add(u)

# a, b = map(int, input().split())


# Suppose the file name is "graph.txt"
with open("test3.txt") as f:
    n, m = map(int, f.readline().split())

    # constructs an undirected graph G of n vertices and m edges
    g = {i: set() for i in range(1, n + 1)}

    for _ in range(m):
        u, v = map(int, f.readline().split())
        g[u].add(v)
        g[v].add(u)
    
# to calculate the number of connected components
def bfs(Adj, s, parent):
    Q = deque()
    Q.append(s)
    while len(Q) != 0:
        u = Q.popleft()
        for v in Adj[u]:
            if v not in parent:
                parent[v] = u
                Q.append(v)
    
    
    
def connectedComponents(Adj):
    # starts from a as a source
    parent = {}
    
    count = 0
    
    for u in Adj:
        if u not in parent:
            count += 1
            parent[u] = None
            bfs(Adj, u, parent)
    return count
            
        

print(connectedComponents(g))          
    