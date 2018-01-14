//同向双指针
//初始化快指针在慢指针后面一位
//当两个指针指向的数不相同时，把快指针的值覆盖到慢指针的下一位，然后慢指针往后移一位
//新数组的长度 = 慢指针index + 1
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 1) {
            return 1;
        }
        
        int slow = 0;
        int fast = 1;
        while (fast < nums.length) {
            if (nums[fast] != nums[slow]) {
                slow++;
                nums[slow] = nums[fast];
            }
            fast++;
        }
        return slow + 1;
    }
}
