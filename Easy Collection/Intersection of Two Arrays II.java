//先sort两个数组
//用两根指针同时遍历两个数组
//两个指针要从两个数组第一个intersect的数字开始
//如果数字相同，两根指针同时后移，记录这个数字
//如果不同，移动数字较小的指针
class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        
        int cur1 = 0;
        int cur2 = 0;
        
        List<Integer> res = new ArrayList<>();
        
        while (true) {
            //初始化指针
            while (cur1 < nums1.length && cur2 < nums2.length && nums1[cur1] != nums2[cur2]) {
                //移动数字较小的指针
                if (nums1[cur1] < nums2[cur2]) {
                    cur1++;
                } else {
                    cur2++;
                }
            }
            if (cur1 >= nums1.length || cur2 >= nums2.length) {
                break;
            }
            else if (nums1[cur1] == nums2[cur2]) {
                res.add(nums1[cur1]);
                cur1++;
                cur2++;
            } else {
                //移动数字较小的指针
                if (nums1[cur1] < nums2[cur2]) {
                    cur1++;
                } else {
                    cur2++;
                }
            }
        }
        
        int[] result = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            result[i] = res.get(i);
        }
        
        return result;
    }
}
