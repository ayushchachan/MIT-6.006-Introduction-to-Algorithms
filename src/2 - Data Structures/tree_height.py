from collections import deque

def tree_height(root, children, n):
    ## we will use bfs to compute depth which is also the height
    
    Q = deque()
    Q.append(root)
    
    max_depth = 0
    
    depth = [-1 for _ in range(n)]
    depth[root] = 0
    
    while len(Q) != 0 :
        u = Q.popleft()
        for v in children[u]:
            if depth[v] == -1:
                depth[v] = depth[u] + 1
                max_depth = max(max_depth, depth[v])
                Q.append(v)
    return max_depth
        
        


# n = int(input("Enter the number of nodes: "))
# parents = list(map(int, input().split()))
## generating the tree

# n = 5
# parents = [4, -1, 4, 1, 1]
# children = [[] for _ in range(n)]

# for i in range(n):
#         p_i = parents[i]
#         if p_i == -1:
#             root = i
#             continue
#         children[p_i].append(i)
# h = tree_height(root, children, n)
# print(h + 1)


# ======== Paste below your tree_height() definition ========

def _build_root_and_children(n, parents):
    children = [[] for _ in range(n)]
    root = None
    for i, p in enumerate(parents):
        if p == -1:
            root = i
        else:
            children[p].append(i)
    return root, children

def _run_tests():
    # Height here is counted in NODES (so single-node tree = 1)
    test_cases = [
        # 1) trivial
        (1, [-1], 1),

        # 2) chains (deep)
        (5,  [-1, 0, 1, 2, 3], 5),                        # 0->1->2->3->4
        (10, [9, 0, 1, 2, 3, 4, 5, 6, 7, -1], 10),        # root at 9, long chain

        # 3) stars (wide, shallow)
        (5,  [-1, 0, 0, 0, 0], 2),                        # star at 0
        (10, [5, 5, 5, 5, 5, -1, 5, 5, 5, 5], 2),         # star at 5
        (12, [-1] + [0]*11, 2),                           # very wide star

        # 4) root not at index 0
        (5,  [4, 4, 4, 4, -1], 2),                        # root=4
        (5,  [3, 3, 3, -1, 1], 3),                        # root=3; path 3→1→4

        # 5) balanced-ish small trees
        (7,  [-1, 0, 0, 1, 1, 2, 2], 3),
        (9,  [-1, 0, 1, 1, 0, 4, 4, 6, 6], 4),

        # 6) mixed shapes
        (6,  [1, 2, -1, 2, 3, 2], 3),                     # root=2; deepest depth=2 → height 3
        (6,  [-1, 0, 1, 2, 3, 2], 5),                     # long chain + side child
        (8,  [-1, 0, 0, 0, 2, 2, 2, 2], 3),
        (7,  [1, 2, 3, -1, 3, 4, 5], 4),

        # 7) tiny sanity checks
        (2,  [-1, 0], 2),
        (2,  [1, -1], 2),
        (3,  [-1, 0, 0], 2),
        (3,  [1, 2, -1], 3),

        # 8) another balanced-ish
        (7,  [2, 2, -1, 0, 0, 3, 3], 4),

        # 9) your example
        (5,  [4, -1, 4, 1, 1], 3),
    ]

    failures = 0
    for idx, (n, parents, expected_height_nodes) in enumerate(test_cases, 1):
        root, children = _build_root_and_children(n, parents)
        max_depth_edges = tree_height(root, children, n)
        got_height_nodes = max_depth_edges + 1
        status = "OK" if got_height_nodes == expected_height_nodes else f"FAIL (got {got_height_nodes})"
        print(f"Test {idx}: n={n}, parents={parents} -> expected {expected_height_nodes}, {status}")
        if status.startswith("FAIL"):
            failures += 1
    print(f"\nDone. Failures: {failures} / {len(test_cases)}")

if __name__ == "__main__":
    _run_tests()
