//nums[right] - nums[left] == right - left时是连续的，满足一个range
class Solution {
    public List<String> summaryRanges(int[] nums) {
        int left = 0;
        int right = 0;
        List<String> res = new ArrayList<>();
        
        while (right < nums.length) {
            while (right < nums.length && nums[right] - nums[left] == right - left) {
                right++;
            }
            //到最后一个元素时，right可能在数组外面，left指向最后一个元素，此时只需要把left指向的数放到res里
            if (nums[left] != nums[right - 1]) {
                res.add(nums[left] + "->" + nums[right - 1]);
            } else {
                res.add(nums[left] + "");
            }
            left = right;
        }
        
        return res;
    }
}
