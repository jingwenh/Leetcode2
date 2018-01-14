// Original List                   : 1 2 3 4 5 6 7
// After reversing all numbers     : 7 6 5 4 3 2 1
// After reversing first k numbers : 5 6 7 4 3 2 1
// After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length; //有病，超过了长度从头接着走，题目里没说
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);      

    }
    
    //相向双指针，两个元素交换
    private void reverse(int[] nums, int start, int end) {
        int left = start;
        int right = end;
        
        while (left <= right) {
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }
    }
}
