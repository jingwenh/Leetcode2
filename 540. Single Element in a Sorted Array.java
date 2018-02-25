//binary search
//不同的是这次用一个长度为2的sliding window做二分查找
//因为总元素个数是单数
//二分查找时，让window左边为偶数个元素，window右边为奇数个元素
//如果window里是一个pair，那么single一定在奇数个数那一边，即右边
//如果window里不是一个pair，那么single元素一定在偶数个数那边，即左边
class Solution {
   public static int singleNonDuplicate(int[] nums) {
        int start = 0, end = nums.length - 1;

        while (start < end) {
            // We want the first element of the middle pair,
            // which should be at an even index if the left part is sorted.
            // Example:
            // Index: 0 1 2 3 4 5 6
            // Array: 1 1 3 3 4 8 8
            //            ^
            int mid = (start + end) / 2;
            //用mid和mid + 1表示一个window，mid必须是偶数才能保证左边偶数个元素，右边奇数个元素
            if (mid % 2 == 1) mid--;

            // We didn't find a pair. The single element must be on the left.
            // (pipes mean start & end)
            // Example: |0 1 1 3 3 6 6|
            //               ^ ^
            // Next:    |0 1 1|3 3 6 6
            if (nums[mid] != nums[mid + 1]) end = mid;//end移到左半边，即0 - 1

            // We found a pair. The single element must be on the right.
            // Example: |1 1 3 3 5 6 6|
            //               ^ ^
            // Next:     1 1 3 3|5 6 6|
            else start = mid + 2; //start移到右半边，即5 - 6
        }

        // 'start' should always be at the beginning of a pair.
        // When 'start > end', start must be the single element.
        return nums[start];
    }
}
