class Solution {
    public int[] twoSum(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int[] origin = Arrays.copyOf(nums, nums.length);
        
        Arrays.sort(nums);
        int[] adds = new int[2];
        
        while (left < right) {
            int sum = nums[left] + nums[right];
            if (sum < target) {
                left++;
            } else if (sum > target) {
                right--;
            } else if (sum == target){
                adds[0] = nums[left];
                adds[1] = nums[right];
                break;
            }
        }
        
        int[] res = new int[2];
        //从前往后扫拿第一个数的index
        for (int i = 0; i < origin.length; i++) {
            if (origin[i] == adds[0]) {
                res[0] = i;
            }
        }
        //从后往前扫拿第二个数的index
        for (int i = origin.length - 1; i >= 0; i--) {
            if (origin[i] == adds[1]) {
                res[1] = i;
            }
        }
        
        
        return res;
    }
}
