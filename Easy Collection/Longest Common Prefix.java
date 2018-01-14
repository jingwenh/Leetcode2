//打擂台
//遍历整个数组，保留每个字符串和当前prefix的common prefix
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        
        String prefix = strs[0];
        for (String s : strs) {
            prefix = getCommonPrefix(prefix, s);
        }
        return prefix;
    }
    
    //找两个字符串的common prefix
    //用两根指针分别遍历两个字符串
    private String getCommonPrefix(String s1, String s2) {
        int cur1 = 0;
        int cur2 = 0;
        String prefix = "";
        while (cur1 < s1.length() && cur2 < s2.length()) {
            if (s1.charAt(cur1) == s2.charAt(cur2)) {
                prefix = prefix + s1.charAt(cur1);
                cur1++;
                cur2++;
            } else {
                break;
            }
        }
        return prefix;
    }
}
