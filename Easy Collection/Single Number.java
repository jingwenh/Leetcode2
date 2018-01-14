//Sort把所有重复的数挤在一起
//扫一遍数组看一个数后面是不是有和它一样的数，有就跳两格，没有就返回这个数
class Solution {
    public int singleNumber(int[] nums) {
        Arrays.sort(nums);
        int cur = 0;
        while (cur + 1 < nums.length) {
            if (nums[cur] == nums[cur + 1]) {
                cur = cur + 2;
            } else {
                return nums[cur];
            }
        }
        //single number在最后一个，循环里找不到这个数，就返回最后一个
        return nums[nums.length - 1];
    }
}
