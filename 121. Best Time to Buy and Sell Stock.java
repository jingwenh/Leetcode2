class Solution {
    //遍历数组
    //当前购买的最大利润 = 右边的最大值 - 当前的价格
    //然后记录总的最大的价格
    public int maxProfit(int[] prices) {
        PriorityQueue<Integer> right = new PriorityQueue<>(7, new IntComparator());
        int maxProfit = 0;
        for (int i : prices) {
            right.offer(i);
        }
        for (int i = 0; i < prices.length - 1; i++) {
            right.remove(prices[i]);
            maxProfit = Math.max(maxProfit, right.peek() - prices[i]);
        }
        return maxProfit;
    }
    
    private class IntComparator implements Comparator<Integer> {
        public int compare(Integer i1, Integer i2) {
            return (i2 - i1);
        }
    }
}
