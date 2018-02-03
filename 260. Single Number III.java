//先sort
//single number可能在3个位置：头，尾，中间
//分别判断三种情况
class Solution {
    public int[] singleNumber(int[] nums) {
        
        Arrays.sort(nums);
        int[] res = new int[2];
        Stack<Integer> stk = new Stack<>();
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && i < nums.length - 1) {
                if (nums[i] != nums[i - 1] && nums[i] != nums[i + 1]) {
                    stk.push(nums[i]);
                }
            } else if (i == 0 && nums[i] != nums[i + 1]) {
                stk.push(nums[i]);
            } else if (i == nums.length - 1 && nums[i] != nums[i - 1]){
                stk.push(nums[i]);
            }
        }
        
        res[0] = stk.pop();
        res[1] = stk.pop();
        return res;
        
    }
}
