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
with open("test2.txt") as f:
    n, m = map(int, f.readline().split())

    # constructs an undirected graph G of n vertices and m edges
    g = {i: set() for i in range(1, n + 1)}

    for _ in range(m):
        u, v = map(int, f.readline().split())
        g[u].add(v)
        g[v].add(u)
    
    u1, u2 = map(int, f.readline().split())

# is a and b are connected

def isConnected(Adj, a, b):
    # starts from a as a source
    s = a
    visited = set()
    visited.add(s)
    Q = deque()
    Q.append(s)
    
    while (len(Q) != 0):
        u = Q.popleft()
        for v in Adj[u]:
            if v == b:
                return True
            if v not in visited:
                Q.append(v)
                visited.add(v)
    return False

print(isConnected(g, u1, u2))          
    