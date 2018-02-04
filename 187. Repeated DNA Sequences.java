//用一个长度为10的sliding window，10位10位地把String放进HashSet里
class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        int left = 0;
        int right = 10;
        //Key是String, value是有没有加到结果集里
        Map<String, Boolean> map = new HashMap<>();
        ArrayList<String> res = new ArrayList<>();
        while (right <= s.length()) {
            String sub = s.substring(left, right);
            if (map.containsKey(sub) && map.get(sub) != true) {
                res.add(sub);
                map.put(sub, true);
            } else if (!map.containsKey(sub)){
                map.put(sub, false);
            }
            left++;
            right++;
        }
        return res;
    }
}
