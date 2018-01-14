//先把字符都放进ASC数组，记录每一个字符出现的次数
//再按顺序重新扫一遍字符串，取出第一个出现次数为1的字符
class Solution {
    public int firstUniqChar(String s) {
        int[] asc = new int[128];
        for (int i = 0; i < s.length(); i++) {
            asc[s.charAt(i)] = asc[s.charAt(i)] + 1;
        }
        
        for (int i = 0; i < s.length(); i++) {
            if (asc[s.charAt(i)] == 1) {
                return i;
            }
        }
        
        return -1;
    }
}
