//思路和266类似
//用hashSet找成对的元素
//最后hashset里剩下的是落单的元素
class Solution {
    public int longestPalindrome(String s) {
        Set<Character> set = new HashSet<>();
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (set.contains(s.charAt(i))) {
                set.remove(s.charAt(i));
                count = count + 2; //每次删除即找到了一对
            } else {
                set.add(s.charAt(i));
            }
        }
        if (set.size() != 0) {
            return count + 1; //set里还有落单的就从中间随便拿一个放中间
        } else {
            return count;
        }
    }
}
