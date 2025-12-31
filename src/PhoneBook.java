import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class PhoneBook {

    private List<LinkedList<Node>> data;
    private int m;                              // size of table

    public PhoneBook() {
        this(37);
    }

    public PhoneBook(int N) {
        data = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            data.add(new LinkedList<>());
        }
        m = N;
    }


    public void add(String name, long number) {
        LinkedList<Node> bucket = data.get(idx(number));
        for (Node n : bucket) {
            if (n.number == number) {
                n.name = name;
                return;
            }
        }
        bucket.add(new Node(name, number));
    }

    public String find(long number) {
        LinkedList<Node> bucket = data.get(idx(number));
        for (Node n : bucket) {
            if (n.number == number) {
                return n.name;
            }
        }
        return "not found";
    }

    public void delete(long number) {
        LinkedList<Node> bucket = data.get(idx(number));
        for (Node n : bucket) {
            if (n.number == number) {
                bucket.remove(n);
            }
        }
        return;
    }

    private int idx(long number) {
        return Math.floorMod(number, this.m);
    }

    private class Node {
        String name;
        long number;

        public Node(String name, long number) {
            this.name = name;
            this.number = number;
        }
    }



    public static void main(String[] args) throws Exception {

        PhoneBook book1 = new PhoneBook();

        String filename = "phonebook_test2.txt";
        BufferedReader br = new BufferedReader(new FileReader("src/" + filename));
        int q = Integer.parseInt(br.readLine().trim());
        for (int i = 0; i < q; i++) {
            String line = br.readLine();
            String[] cmd = line.trim().split("\\s+", 3);
//            System.out.println("cmd = " + Arrays.toString(cmd));

            switch (cmd[0]) {

                case "del":
                    book1.delete(Long.parseLong(cmd[1]));
                    break;


                case "add":
                    book1.add(cmd[2], Long.parseLong(cmd[1]));
                    break;

                case "find":
                    String name = book1.find(Long.parseLong(cmd[1]));
                    System.out.println(name);
                    break;

                default:
                    // optional: handle invalid commands
                    System.out.println("Unknown command: " + cmd);
            }
        }

    }
}
