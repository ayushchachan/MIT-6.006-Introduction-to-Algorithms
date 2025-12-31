def dfs_visit(s, Adj, color, order):
    color[s] = 1
    # print("dfs_visit called with s =", s)
    # print("Adj =", Adj)
    # print("color =", color)

    for v in Adj[s]:
        if color[v] == 0:       ## i.e. not visited yet
            is_acyclic = dfs_visit(v, Adj, color, order)
            if not is_acyclic:
                return False
        elif color[v] == 1:
            # print("dfs_visit exit with cycle s =", s)
            return False
    color[s] = 2
    # print("dfs_visit exit without cycle s =", s)
    order.append(s)
    return True


def full_dfs(Adj, order = []):
    color = {}
    for u in Adj:
        color[u] = 0        ## initially all vertices will be white colored i.e. not visited yet
    
    order = []      ## topological ordering
    
    for u in Adj:
        if color[u] == 0:
            is_acyclic = dfs_visit(u, Adj, color, order)
            if not is_acyclic:
                return False
    return True

topological_order = []
# full_dfs(g, topological_order)