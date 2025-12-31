import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class ChainHashing {

    private List<LinkedList<String>> data;
    private int m;                              // size of table

    public ChainHashing() {
        this(37);
    }

    public ChainHashing(int numBuckets) {
        data = new ArrayList<>();
        for (int i = 0; i < numBuckets; i++) {
            data.add(new LinkedList<>());
        }
        m = numBuckets;
    }


    public void add(String newData) {
        LinkedList<String> bucket = data.get(idx(newData));
        for (String s : bucket) {
            if (s.equals(newData)) {
                return;
            }
        }
        bucket.addFirst(newData);
    }

    public String find(String newData) {
        LinkedList<String> bucket = data.get(idx(newData));
        for (String s : bucket) {
            if (s.equals(newData)) {
                return "yes";
            }
        }
        return "no";
    }

    public String checkBucket(int i) {
        return data.get(i).toString();
    }

    public void delete(String newData) {
        LinkedList<String> bucket = data.get(idx(newData));
        for (String s : bucket) {
            if (s.equals(newData)) {
                bucket.remove(s);
                return;
            }
        }
    }

    private int idx(String s) {
        int p = 1000000007;
        int x = 263;

        int n = s.length();

        long h = 0;
        for (int i = 0; i < n; i++) {
            h = h * x + s.charAt(n - 1 - i);
            h = Math.floorMod(h, p);
        }
        return Math.floorMod(h, this.m);
    }







    public static void main(String[] args) throws Exception {


        String filename = "chainhashing_test3.txt";
        BufferedReader br = new BufferedReader(new FileReader("test/" + filename));

        int m = Integer.parseInt(br.readLine().trim());
        ChainHashing book1 = new ChainHashing(m);


        int q = Integer.parseInt(br.readLine().trim());
        for (int i = 0; i < q; i++) {
            String line = br.readLine();
            String[] cmd = line.trim().split("\\s+", 3);
//            System.out.println("cmd = " + Arrays.toString(cmd));

            switch (cmd[0]) {

                case "del":
                    book1.delete(cmd[1]);
                    break;


                case "add":
                    book1.add(cmd[1]);
                    break;

                case "find":
                    String name = book1.find(cmd[1]);
                    System.out.println(name);
                    break;

                case "check":
                    int j = Integer.parseInt(cmd[1]);
                    System.out.println(book1.checkBucket(j));
                    break;

                default:
                    // optional: handle invalid commands
                    System.out.println("Unknown command: " + cmd);
            }
        }

    }
}
