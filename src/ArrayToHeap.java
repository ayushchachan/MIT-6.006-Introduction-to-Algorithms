import java.util.Scanner;

public class ArrayToHeap {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] A = new int[n];

        for (int i = 0; i < n; i++) {
            A[i] = sc.nextInt();
        }

        int lastIndex = n - 1;

        for (int k = (lastIndex - 1) / 2 ; k >= 0 ; k--) {
            int i = k;
            while (i <= lastIndex / 2) {
                // perform Heapify(A, i)
                int left = 2 * i + 1;
                int right = 2 * i + 2;

                int smallest = i;

                if (left < n && A[left] < A[i]) {
                    smallest = left;
                }

                if (right < n && A[right] < A[smallest]) {
                    smallest = right;
                }

                if (smallest != i) {
                    System.out.println(i + " " + smallest);

                    int temp = A[smallest];
                    A[smallest] = A[i];
                    A[i] = temp;

                    // update i
                    i = smallest;

                } else {
                    break;
                }




            }
        }
    }
}
