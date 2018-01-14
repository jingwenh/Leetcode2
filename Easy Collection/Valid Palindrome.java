public class Solution {
     //相向双指针
     //先把标点符号去掉，所有大写字母转换成小写
     //再用相向双指针判断
     //比较左指针和右指针指向的元素是否相同
     //两个指针相遇时结束循环
    public boolean isPalindrome(String s) {
        StringBuilder sRemovePunc = new StringBuilder();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (isValid(c)) {
                sRemovePunc.append(Character.toLowerCase(c));
            }
        }
        
        int left = 0;
        int right = sRemovePunc.length() - 1;        
        
        while(left <= right) {
            if (sRemovePunc.charAt(left) != sRemovePunc.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }
    
    private boolean isValid (char c) {
        return Character.isLetter(c) || Character.isDigit(c);
    }
}
