
public class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode x = root;

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);

            if (x.children[c - 'a'] == null) {
                x.children[c - 'a'] = new TrieNode();
            }
            x = x.children[c - 'a'];

        }
        x.isEndOfWord = true;

    }

    public boolean search(String word) {
        TrieNode x = root;

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);

            if (x.children[c - 'a'] == null) {
                return false;
            }
            x = x.children[c - 'a'];
        }
        return x.isEndOfWord;
    }

    public boolean startsWith(String prefix) {
        TrieNode x = root;

        for (int i = 0; i < prefix.length(); i++) {
            char c = prefix.charAt(i);

            if (x.children[c - 'a'] == null) {
                return false;
            }
            x = x.children[c - 'a'];
        }
        return true;
    }

    public static void main(String[] args) {

    }

    static class TrieNode {
        TrieNode[] children;
        boolean isEndOfWord;

        public TrieNode() {
            children = new TrieNode[26];
            this.isEndOfWord = false;
        }
    }
}



/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
