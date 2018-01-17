class Solution {
    //如果两个词是anagram, 分别对两个词的字母排序，会得到两个相同的字符串
    //利用这个性质，把每个词放进HashMap, 用排序后得到的单词当做key，value是list
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String s : strs) {
            String key = sortChar(s);
            if (map.containsKey(key)) {
                List<String> list = map.get(key);
                list.add(s);
            } else {
                List<String> list = new ArrayList<>();
                list.add(s);
                map.put(key, list);
            }
        }
        
        List<List<String>> res = new ArrayList<>();
        for (String key : map.keySet()) {
            res.add(map.get(key));
        }
        
        return res;
    }
    
    private String sortChar(String str) {
        StringBuilder res = new StringBuilder();
        
        Queue<Character> pq = new PriorityQueue<>();
        for (int i = 0; i < str.length(); i++) {
            pq.offer(str.charAt(i));
        }
        while (!pq.isEmpty()) {
            res.append(pq.poll());
        }
        
        
        return new String(res);
    }
}
