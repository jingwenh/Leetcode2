class Solution {

    int[] nums;
    private int[] copy; //nums可能会被shuffle, 要copy一下原数组
    
    public Solution(int[] nums) {
        this.nums = nums;
        this.copy = nums.clone();
    }
    
    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        return copy;
    }
    
    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        Random random = new Random();
        for (int i = nums.length - 1; i > 0; i--) { //遍历每一个数，每一个数都和一个数组里随机位置的一个数交换
            int j = random.nextInt(i + 1);
            int t = nums[i];
            nums[i] = nums[j];
            nums[j] = t;
        }
        return nums;        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */
