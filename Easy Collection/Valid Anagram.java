//用两个asc数组分别表示两个字符串
//asc一样说明是anagram，否则不是
class Solution {
    public boolean isAnagram(String s, String t) {
        int[] asc1 = new int[128];
        int[] asc2 = new int[128];
        
        for (int i = 0; i < s.length(); i++) {
            asc1[s.charAt(i)] = asc1[s.charAt(i)] + 1;
        }
        for (int i = 0; i < t.length(); i++) {
            asc2[t.charAt(i)] = asc2[t.charAt(i)] + 1;
        }
        
        for (int i = 0; i < 128; i++) {
            if (asc1[i] != asc2[i]) {
                return false;
            }
        }
        return true;
    }
}
