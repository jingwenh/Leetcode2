class Solution {
    //遍历数组
    //记录三个值：前缀和，当前最大的sum，以及当前最小的sum
    //前缀和 = 按顺序依次累加
    //最大sum = Math.max(前缀和 - 上一个最小sum, 上一个最大sum)
    //最小sum = Math.min(前缀和, 上一个最小sum)
    public int maxSubArray(int[] A) {
        if (A == null || A.length == 0){
            return 0;
        }
        
        int max = Integer.MIN_VALUE, sum = 0, minSum = 0;
        for (int i = 0; i < A.length; i++) {
            sum += A[i];
            //记录最大值和最小值
            //最大值在（sum - 上一个最小值）中取
            max = Math.max(max, sum - minSum);
            //最小值在sum里面取
            minSum = Math.min(minSum, sum);            
        }

        return max;
    }
}
