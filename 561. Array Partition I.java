class Solution {
    //先sort，把接近的数都靠在一起
    //然后按顺序两两组队，把较小的那个数加到sum上
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int left = 0;
        int right = 1;
        int sum = 0;
        while (right < nums.length) {
            sum = sum + Math.min(nums[left], nums[right]);
            left = left + 2;
            right = right + 2;
        }
        return sum;
    }
}
