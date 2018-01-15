class Solution {
    //倒着merge，把较大的数从A的尾部插入
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int cur1 = m - 1;
        int cur2 = n - 1;
        int cur = nums1.length - 1;
        
        while (cur1 >= 0 && cur2 >= 0) {
            if (nums1[cur1] > nums2[cur2]) {
                nums1[cur] = nums1[cur1];
                cur--;
                cur1--;
            } else {
                nums1[cur] = nums2[cur2];
                cur--;
                cur2--;                
            }
        }
        
        while (cur1 >= 0) {
            nums1[cur] = nums1[cur1];
            cur--;
            cur1--;           
        }
        while (cur2 >= 0) {
            nums1[cur] = nums2[cur2];
            cur--;
            cur2--;            
        }
    }
}
