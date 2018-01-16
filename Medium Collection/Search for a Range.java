//[5, 7, 7, 8, 8, 8, 8, 10]
//8
//两次binary search
//第一次优先丢左半边，取最后一个end指针，得到lower bound
//第二次优先丢右半边，取最后一个start指针，得到upper bound
class Solution {
    public int[] searchRange(int[] nums, int target) {
        if (nums.length == 0) {
            int[] res = {-1, -1};
            return res;
        }
        
        int[] res = new int[2];
        res[1] = bsUB(nums, target);
        res[0] = bsLB(nums, target);
        return res;
    }
    
    private int bsUB(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (nums[mid] > target) {
                end = mid;
            }
            if (nums[mid] == target) {
                start = mid;
            }
            if (nums[mid] < target) {
                start = mid;
            }
        }
        
        if (nums[end] == target) {
            return end;
        } else if (nums[start] == target) {
            return start;
        } else {
            return -1;
        }
    }
    
    private int bsLB(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (nums[mid] > target) {
                end = mid;
            }
            if (nums[mid] == target) {
                end = mid;
            }
            if (nums[mid] < target) {
                start = mid;
            }
        }
        
        if (nums[start] == target) {
            return start;
        } else if (nums[end] == target) {
            return end;
        } else {
            return -1;
        }        
    }
}
