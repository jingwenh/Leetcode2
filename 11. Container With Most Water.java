class Solution {
    //最大盛水量取决于短板
    //S = abs(index2 - index2) * min(h2, h1)
    //相向双指针，每次都移动较短的那一边，然后记录一个最大盛水量
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxWater = 0;
        while (left + 1 <= right) { //记得加等号，不然两个指针相邻的case没有计算就直接出来了
            int volume = (right - left) * Math.min(height[left], height[right]);
            maxWater = Math.max(maxWater, volume);
            if (height[left] > height[right]) {
                right--;
            } else {
                left++;
            }
        }
        return maxWater;
    }
}
