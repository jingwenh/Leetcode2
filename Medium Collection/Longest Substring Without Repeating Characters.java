class Solution {
    public int lengthOfLongestSubstring(String s) {
        Queue<Integer> pq = new PriorityQueue<>(7, new IntComparator());
        pq.offer(0);
        
        for (int i = 0; i < s.length(); i++) {
            String sub = s.substring(i);
            pq.offer(maxLen(sub));
            if (pq.peek() >= sub.length()) {
                break;
            }
        }
        return pq.poll();
    }
    
    //找从第一个字符开头的最长不重复字符串
    private int maxLen(String s) {
        int len = 0;
        Set<Character> set = new HashSet<>();
        for (int i = 0; i < s.length(); i++) {
            if (set.contains(s.charAt(i))) { //出现重复字符，返回上一个串的长度，重置set
                return len;
            } else { //否则len++，并把新出现的字符放进set
                set.add(s.charAt(i));
                len++;
            }
        }
        return len;
    }
    
    private class IntComparator implements Comparator<Integer> {
        public int compare(Integer i1, Integer i2) {
            return i2 - i1;
        }
    }
}
