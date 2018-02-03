class Solution {
    public int titleToNumber(String s) {
        int cur = s.length() - 1;
        int res = 0;
        int pow26 = 1;
        while (cur >= 0) {
            char c = s.charAt(cur);
            res = res + getNum(c) * pow26;
            pow26 = pow26 * 26;
            cur--;
        }
        return res;
    }
    
    private int getNum(char c) {
        return c - 64;
    }
}
