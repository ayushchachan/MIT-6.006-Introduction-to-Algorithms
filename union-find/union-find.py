import time                     # Used for high-precision timing
import pandas as pd            # Used for storing results and plotting
import matplotlib.pyplot as plt  # Used for graph visualization



class UnionFind:
    """A simple union-find (disjoint set) implementation.

    This implementation uses the simple-union strategy.
    Each element starts in its own component, and components are merged by
    linking the root of one component to the root of another.
    """

    def __init__(self, N):
        """Initialize the union-find structure for N items.
        """
        self.parent = [i for i in range(N)]
        self.size = [1 for i in range(N)]
        self.num_connected_components = N
    

    def union(self, p, q):
        """Connect the components containing p and q.

        If p and q are already in the same component, this is a no-op.
        Otherwise, it links the root of q's component to the root of p's
        component and decrements the component count.
        """
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return

        self.parent[q_root] = p_root
        self.num_connected_components -= 1
        

    def find(self, p):
        """Return the root identifier for the component containing p.

        This walks up the parent links until it reaches a root element,
        where the element is its own parent.
        """
        while self.parent[p] != p:
            p = self.parent[p]
        return p


    def count(self):
        """Return the number of connected components."""
        return self.num_connected_components


    def isConnected(self, p, q):
        """Return True if p and q are in the same component."""
        return self.find(p) == self.find(q)



class UnionFind2(UnionFind):
    """A simple union-find (disjoint set) implementation.

    This implementation uses the weighted union strategy.
    Each element starts in its own component, and components are merged by
    linking the root of smaller component to the root of larger component.
    """

    def union(self, p, q):
        """Connect the components containing p and q.

        If p and q are already in the same component, this is a no-op.
        Otherwise, it links the root of q's component to the root of p's
        component and decrements the component count.
        """
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return

        if self.size[p_root] < self.size[q_root]:
            self.parent[p_root] = q_root
            self.size[q_root] += self.size[p_root]
        else:
            self.parent[q_root] = p_root
            self.size[p_root] += self.size[q_root]

        self.num_connected_components -= 1


class UnionFind3(UnionFind2):
    """A simple union-find (disjoint set) implementation.

    This implementation uses the weighted union strategy with Full Path Compression (Classic).
    Each element starts in its own component, and components are merged by
    linking the root of smaller component to the root of larger component.
    """

    def find(self, p):
        """Return the root identifier for the component containing p.

        This walks up the parent links until it reaches a root element,
        where the element is its own parent.
        """
        root = p
        while self.parent[root] != root:
            root = self.parent[root]
        
        while p != root:
            temp = self.parent[p]
            self.parent[p] = root
            p = temp
        
        return root


class UnionFind4(UnionFind2):
    """A simple union-find (disjoint set) implementation.

    This implementation uses the weighted union strategy with Path Compression by Halving.
    Each element starts in its own component, and components are merged by
    linking the root of smaller component to the root of larger component.
    """

    def find(self, p):
        """Return the root identifier for the component containing p.

        This walks up the parent links until it reaches a root element,
        where the element is its own parent.
        """
        while self.parent[p] != p:
            # make p point to its grand-parent
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p


# -------------------------------
# Function to load input file
# -------------------------------
def load_data(filename):
    """
    Reads the file and returns:
    - N: number of elements
    - pairs: list of (p, q) union operations
    """
    with open(filename, "r") as file_object:
        # The first line is the number of elements in the union-find structure.
        N = int(file_object.readline())

        pairs = []
        for line in file_object:
            if line.strip():
                p, q = map(int, line.split())
                pairs.append((p, q))
    return N, pairs


# -------------------------------
# Function to benchmark one UF
# -------------------------------
def benchmark(uf_class, N, pairs):
    """
    Runs union-find operations and measures time.
    
    uf_class : class (UnionFind, UnionFind2, etc.)
    N        : number of elements
    pairs    : list of union operations
    """
    uf = uf_class(N)

    start_time = time.perf_counter()

    for p, q in pairs:
        uf.union(p, q)
    
    end_time = time.perf_counter()

    # Print the number of connected components after processing all pairs.
    # print(uf.count(), "connected components")
    return (end_time - start_time)


# -------------------------------
# Input files
# -------------------------------
input_files = ["tinyUF.txt", "mediumUF.txt", "largeUF.txt"]

#store results here
results = []

# -------------------------------
# Main benchmarking loop
# -------------------------------
for filename in input_files:

        ## load data once
        N, pairs = load_data(filename)

        
        
        # measure each implementation
        t2 = benchmark(UnionFind2, N, pairs)
        t3 = benchmark(UnionFind3, N, pairs)
        t4 = benchmark(UnionFind4, N, pairs)

        # Store results
        results.append({
            "file": filename,
            "WeightedUnionFind": t2,
            "WeightedUnionFind-full-path-compression": t3,
            "WeightedUnionFind-path-compression-by-halving": t4
        })


# -------------------------------
# Convert to Pandas DataFrame
# -------------------------------
df = pd.DataFrame(results)

# Set file as index for better plotting
df.set_index("file", inplace=True)

print("\nPerformance Table:\n")
print(df)

# ============================================================
# 🔥 ADDITIONAL EXPERIMENT: RANDOM INPUT (NO LIVE PLOT)
# ============================================================

import numpy as np

# -------------------------------
# Generate random pairs (vectorized)
# -------------------------------
def generate_random_pairs(N, num_ops):
    """
    Generates random (p, q) pairs using NumPy.
    Much faster than Python random.
    """
    p = np.random.randint(0, N, size=num_ops, dtype=np.int32)
    q = np.random.randint(0, N, size=num_ops, dtype=np.int32)
    return p, q


# -------------------------------
# Benchmark using NumPy arrays
# -------------------------------
def benchmark_numpy(uf_class, N, p_array, q_array):
    """
    Runs union operations on pre-generated arrays.
    """
    uf = uf_class(N)

    start = time.perf_counter()

    # Iterate through arrays
    for i in range(len(p_array)):
        uf.union(int(p_array[i]), int(q_array[i]))

    end = time.perf_counter()

    return end - start


# -------------------------------
# Experiment configuration
# -------------------------------
N = 1_000_000   # number of elements

operation_sizes = [
    50_000,
    100_000,
    500_000,
    1_000_000,
    2_000_000,
    5_000_000,
    10_000_000,
    20_000_000,
    50_000_000,
]

# Store results
sizes = []
times_uf2 = []
times_uf3 = []
times_uf4 = []

print("\nRunning RANDOM INPUT benchmark...\n")

# -------------------------------
# Run experiment (NO plotting here)
# -------------------------------
for ops in operation_sizes:
    print(f"Processing {ops} operations...")

    # Generate SAME data for all algorithms (important!)
    p_array, q_array = generate_random_pairs(N, ops)

    # Benchmark
    t2 = benchmark_numpy(UnionFind2, N, p_array, q_array)
    t3 = benchmark_numpy(UnionFind3, N, p_array, q_array)
    t4 = benchmark_numpy(UnionFind4, N, p_array, q_array)

    # Store results
    sizes.append(str(ops))
    times_uf2.append(t2)
    times_uf3.append(t3)
    times_uf4.append(t4)


# -------------------------------
# Create DataFrame
# -------------------------------
df_random = pd.DataFrame({
    "Operations": sizes,
    "Weighted": times_uf2,
    "Full Compression": times_uf3,
    "Halving": times_uf4
})

print("\nRandom Input Performance Table:\n")
print(df_random)


# -------------------------------
# Plot AFTER everything is done
# -------------------------------
plt.figure()

plt.plot(sizes, times_uf2, marker='o', label="Weighted Union Find")
plt.plot(sizes, times_uf3, marker='o', label="With Full path Compression")
plt.plot(sizes, times_uf4, marker='o', label="With Halving")

plt.xlabel("Number of Operations")
plt.ylabel("Running Time (seconds)")
plt.title("Union-Find Performance (Random Input)")

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()