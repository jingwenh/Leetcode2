class Solution {
    //当元素为n时，数组里必须有n + 1个n才能满足条件
    //比如回答3的有2只兔子，那么必须有4只回答3的兔子才能保持一致
    //即在这种情况下应该回答3但是没回答的有2只兔子
    //比如回答3的有4只兔子，则回答3的兔子数量正好合适
    //比如回答3的有5只兔子，则回答3的兔子数量多了一只，则需要再补3只没回答的兔子
    //问题转化为计算出未回答的兔子数量
    //1. 统计每个数字的数量
    //2. 用(n + 1) - (value % (key + 1))得到没有回答的兔子数量 （如果余数为0，则不需要再增加没回答的兔子）
    //3. 所有未回答的兔子数 + 数组长度 = 最少数量
    
    public int numRabbits(int[] answers) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i : answers) {
            if (!map.containsKey(i)) {
                map.put(i, 1);
            } else {
                int count = map.get(i);
                map.put(i, count + 1);
            }
        }
        
        int unanswered = 0;
        for (int i : map.keySet()) {
            int count = map.get(i);
            int extra = count % (i + 1);
            if (extra > 0) {
                unanswered = unanswered + (i + 1 - count % (i + 1));
            }
        }
        
        return unanswered + answers.length;
    }
}
