class Solution {
    public String countAndSay(int n) {
        String s = "1";
        for (int i = 0; i < n - 1; i++) {
            s = say(s);
        }
        
        return s;
    }
    
    //读出输入的字符串
    //同向双指针，慢指针记录字符，快指针数字符数量
    private String say(String s) {
        int left = 0;
        int right = 0;
        String say = "";
        while (right < s.length()) {
            int count = 0;
            while (right < s.length() && s.charAt(left) == s.charAt(right)) {
                count++;
                right++;
            }
            say = say + count + "" + s.charAt(left);
            left = right;
        }
        return say;
    }
}
