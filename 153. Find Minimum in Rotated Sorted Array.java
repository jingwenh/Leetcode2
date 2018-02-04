//直接mid和最右边的元素比较
//大于抛左边，小于抛右边
class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[nums.length - 1]) {
                left = mid;
            } else {
                right = mid;
            }
        }
        if (nums[left] > nums[right]) {
            return nums[right];
        } else {
            return nums[left];
        }
    }
}
