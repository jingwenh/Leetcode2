class Solution {
    public String longestPalindrome(String s) {
        String str = "";
        int len = 0;
        for (int i = 0; i < s.length(); i++) {
            for (int j = s.length(); j >= i; j--) {
                String sub = s.substring(i,j);
                if (isPalindrome(sub) && sub.length() > len) {
                    len = Math.max(len, sub.length());
                    str = sub;
                    System.out.println(str);
                }                
            }

        }
        return str;
    }

    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;        
        
        while(left <= right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }
    
}
