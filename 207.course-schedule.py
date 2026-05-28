#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        N = numCourses
        adj = [[] for _ in range(N)]
        for a, b in prerequisites:
           adj[b].append(a)
        
        return full_dfs(adj)

def full_dfs(adj):
    N = len(adj)
    parent = {}

    ## None = white color
    color = [None for _ in range(N)]

    for s in range(N):
        if color[s] is None:
            parent[s] = None
            is_acyclic = dfs_visit(adj, s)
            if not is_acyclic:
                return False
    return True

def dfs_visit(adj, s, color):
    color[s] = 0        ## grayed
    
    for u in adj[s]:
        if color[u] == None:
            ## white colored
            is_acyclic = dfs_visit(adj, u, color)
            if not is_acyclic:
                return False
        elif color[u] == 0:
            return False
    color[s] = 1            ## black colored

# @lc code=end

