public class ReverseInteger {
    public static void main(String[] args) {
        int a = -123;
        Solution S = new Solution();
        System.out.println(S.reverse(a));

    }
}

class Solution {
    public int reverse(int x) {
        boolean isNegative = false;

        if (x < 0) {
            isNegative = true;
            x = -1 * x;

            if (x < 0) return 0;
        }
        long z = 1;

        int y = x;
        while (y != 0) {
            z = z * 10;
            y = y / 10;
        }

        y = x;
        long answer = 0;
        while (y != 0) {
            z = z / 10;
            answer +=  (y % 10) * z;
            y = y / 10;
        }

        if (isNegative) {
            if (answer - 1 > Integer.MAX_VALUE) {
                return 0;
            }
            return -((int)answer);
        } else {
            if (answer > Integer.MAX_VALUE) {
                return 0;
            }
        }
        return (int)answer;

    }
}
