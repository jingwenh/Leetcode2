//同向双指针
//慢指针依次后移
//快指针找非0元素，找到就和慢指针元素交换，然后慢指针向后移一格
class Solution {
    public void moveZeroes(int[] nums) {
        int left = 0;
        int right = 0;
        while (right < nums.length) {
            if (nums[right] != 0) {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                left++;
            }
            right++;
        }
    }
}
