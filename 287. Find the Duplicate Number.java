//先sort, 然后双指针
class Solution {
    public int findDuplicate(int[] nums) {
        Arrays.sort(nums);
        int left = 0;
        int right = 1;
        while (right < nums.length) {
            if (nums[left] != nums[right]) {
                left++;
                right++;
            } else {
                return nums[left];
            }
        }
        return -1;
    }
}
