//只需要找是不是有落单的字符，如果落单的字符超过2个，就不能构成回文
//把字符按顺序放进set
//set里存在这个字符就删去，不存在就放进去
//如果是成对的字符，在遍历结束后set里就不会有这个字符
//最后如果set长度不是0，说明有落单的字符
class Solution {
    public boolean canPermutePalindrome(String s) {
        Set<Character> set = new HashSet<>();
        for (int i = 0; i < s.length(); i++) {
            if (set.contains(s.charAt(i))) {
                set.remove(s.charAt(i));
            } else {
                set.add(s.charAt(i));
            }
        }
        if (set.size() > 1) {
            return false;
        } else {
            return true;
        }
    }
}
