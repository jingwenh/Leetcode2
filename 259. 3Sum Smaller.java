//a + b + c < target 即 a + b < target - c
//计算符合要求的结果个数需要特殊处理
//比如排序后的数组为 1 2 3 4 5, target = 7
//当i = 0时，left = 1, right = 4, right向左移一位以后找到第一个解
//即当i = 0, left = 1, right = 3时有第一个解
//而left到right中间有比nums[right]更小的数，这些数都符合解
//即此时找到的解的个数为 right - left
class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        Arrays.sort(nums);
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            int c = nums[i];
            int left = i + 1;
            int right = nums.length - 1;
            int aim = target - c;
            while (left < right) {
                int sum = nums[left] + nums[right];
                //小于时计数器++
                if (sum < aim) {
                    count = count + (right - left);
                    left++;
                } else if (sum >= aim) {
                    right--;
                }
            }
        }
        return count;
    }
}
