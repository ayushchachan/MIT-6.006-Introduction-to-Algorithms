import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class ParallelProcessing {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();       // Number of Threads
        int m = sc.nextInt();       // Number of jobs

        PriorityQueue<ThreadInfo> Q = new PriorityQueue<>(new ThreadComparator());

        for (int i = 0; i < n; i++) {
            Q.add(new ThreadInfo(i, 0));
        }

        int[] jobs = new int[m];

        for (int i = 0; i < m; i++) {
            jobs[i] = sc.nextInt();

        }

        for (int i = 0; i < m; i++) {
            int jobTime = jobs[i];

            ThreadInfo t = Q.poll();

            System.out.println(t.id + " " + t.nextFreeTime);

            t.nextFreeTime += jobTime;

            Q.add(t);

        }



    }

    static class ThreadInfo {
        int id;
        long nextFreeTime;

        public ThreadInfo(int id, int nextFreeTime) {
            this.id = id;
            this.nextFreeTime = nextFreeTime;
        }
    }

    static class ThreadComparator implements Comparator<ThreadInfo> {

        public int compare(ThreadInfo t1, ThreadInfo t2) {
            if (t1.nextFreeTime != t2.nextFreeTime) {
                return Long.compare(t1.nextFreeTime, t2.nextFreeTime);
            }
            return Integer.compare(t1.id, t2.id);

        }
    }
}
