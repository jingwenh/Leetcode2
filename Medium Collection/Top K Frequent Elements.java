class Solution {
    private class Number {
        int num;
        int freq;
        Number(int num, int freq) {
            this.num = num;
            this.freq = freq;
        }
    }
    
    private class NumComparator implements Comparator<Number> {
        public int compare(Number n1, Number n2) {
            return n2.freq - n1.freq;
        }
    }
    
    public List<Integer> topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i : nums) {
            if (map.containsKey(i)) {
                int freq = map.get(i);
                map.put(i, freq + 1);
            } else {
                map.put(i, 1);
            }
        }
        
        Queue<Number> pq = new PriorityQueue<>(7, new NumComparator());
        for (int i : map.keySet()) {
            Number n = new Number(i, map.get(i));
            pq.offer(n);
        }
        
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            res.add(pq.poll().num);
        }
        
        return res;
    }
}
