class Solution {
    //sort以后相向双指针
    //中间的元素一定是majority
    //比如极端情况，majority是最小的元素
    //[1 1 1 2 3]
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length/2];
    }
}
