//HashMap
class Solution {
    public List<Integer> majorityElement(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        List<Integer> res = new ArrayList<>();
        for (int i : nums) {
            if (map.containsKey(i)) {
                int count = map.get(i);
                map.put(i, count + 1);
            } else {
                map.put(i, 1);
            }           
        }
        
        for (int i : map.keySet()) {
            if (map.get(i) > nums.length / 3) {
                res.add(i);
            }
        }
        
        return res;
    }
}
