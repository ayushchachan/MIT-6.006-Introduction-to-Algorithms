import java.util.Scanner;

public class MergingTables {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int nTables = sc.nextInt();
        int nQueries = sc.nextInt();

        int maxSize = 0;

        int[] parent = new int[nTables];
        int[] size = new int[nTables];

        for (int i = 0; i < nTables; i++) {
            size[i] = sc.nextInt();
            if (size[i] > maxSize) {
                maxSize = size[i];
            }
            parent[i] = i;
        }



        for (int i = 0; i < nQueries; i++) {
            int destination = sc.nextInt() - 1;
            int source = sc.nextInt() - 1;

            // merge source into destination
            while (source != parent[source]) {
                source = parent[source];
            }

            while (destination != parent[destination]) {
                destination = parent[destination];
            }

            if (source != destination) {
                int sourceSize = size[source];
                parent[source] = destination;
                size[destination] += sourceSize;
                size[source] = -1;
                if (size[destination] > maxSize) {
                    maxSize = size[destination];
                }
            }


            System.out.println(maxSize);
        }



    }
}
