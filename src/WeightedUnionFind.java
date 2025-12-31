public class WeightedUnionFind {
    private int[] parent;
    private int[] size;

    private int count;              //  number of connected components

    public WeightedUnionFind(int n) {
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }

        count = n;
    }

    /**
     *
     * return the identifier of ith node
     * @param i the ith node
     * @return the identifier of ith node
     */
    public int find(int i) {
        while (parent[i] != i) {
            i = parent[i];
        }
        return i;

    }

    /**
     *
     * @return the number of connected components
     */
    public int count() {
        return this.count;
    }

    public boolean connected(int a, int b) {
        return this.find(a) == this.find(b);
    }


    public int union(int p, int q) {
        int rootP = this.find(p);
        int rootQ = this.find(q);

        if (rootP == rootQ) {
            return rootP;
        }

                                                    // if p_subtree is smaller
        if (size[rootP] < size[rootQ]) {
            parent[rootP] = rootQ;
            size[rootQ] += size[rootP];
            count--;
            return rootQ;
        } else {                                    // if p_subtree is larger
            parent[rootQ] = rootP;
            size[rootP] += size[rootQ];
            count--;
            return rootP;
        }

    }


    public static void main(String[] args) {

    }
}
