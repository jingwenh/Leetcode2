class Solution {
    public void sortColors(int[] nums) {
        int start = partition(nums, 0, 0);
        partition(nums, start, 1);
    }
    
    private int partition(int[] nums, int start, int target) {
        int left = start;
        int right = nums.length - 1;
        while (left <= right) {
            while (left <= right && nums[left] == target) {
                left++;
            }
            while (left <= right && nums[right] != target) {
                right--;
            }
            if (left <= right) {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                left++;
                right--;                
            }

        }
        
        return left;
    }
}
