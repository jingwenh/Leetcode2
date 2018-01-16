//1 2 3 2 1 4 2 1
//1 2 3
class Solution {
    public int findPeakElement(int[] nums) {
        
        int left = 0;
        int right = nums.length - 1;
        
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid - 1] < nums[mid] && nums[mid] > nums[mid + 1]) { //Peak
                return mid;
            } 
            if (nums[mid - 1] > nums[mid] && nums[mid] < nums[mid + 1]) { //Valley
                left = mid;
            } 
            if (nums[mid - 1] < nums[mid] && nums[mid] < nums[mid + 1]) { //Increase
                left = mid;
            } 
            if (nums[mid - 1] > nums[mid] && nums[mid] > nums[mid + 1]) { //Decrease
                right = mid;
            }
            
        }
        
        if (nums[left] > nums[right]) {
            return left;
        } else {
            return right;
        }
    }
}
