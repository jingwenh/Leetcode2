//维护一个长度为k的最小堆，当长度超过k时，把堆顶（最小的数）移除，这样堆顶始终是第k大的数
class Solution {
    public int findKthLargest(int[] nums, int k) {
        Queue<Integer> pq = new PriorityQueue<>();
        for (int i : nums) {
            pq.offer(i);
            if (pq.size() > k) {
                pq.poll();
            }
        }
        return pq.poll();
    }
}
