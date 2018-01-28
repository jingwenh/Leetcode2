class Solution {
    public int[] productExceptSelf(int[] nums) {
        int total = 1;
        int zeros = 0;
        for (int i : nums) {
            if (i != 0) {
                total = total * i;
            } else {
                zeros++;
            }
            
        }
        //1个0时，除了是0的那一位正常，其它位都是0
        int[] product = new int[nums.length]; 
        if (zeros == 1) {
            for (int i = 0; i < nums.length; i++) {
                if (nums[i] != 0) {
                    product[i] = 0;
                } else {
                    product[i] = total;
                }
            }
            return product;
        }
        //超过1个0，所有位都是0
        if (zeros > 1) {
            return product;
        }
        
        for (int i = 0; i < nums.length; i++) {
            product[i] = total/nums[i];
            
        }
        return product;
    }
}
