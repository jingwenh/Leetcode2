class Solution {
    public int[] plusOne(int[] digits) {
        //腾出一个空间放可能多出来的数位（比如999 + 1 = 1000多了一位）
        int[] res = new int[digits.length + 1];
        for (int i = 1; i <= digits.length; i++) {
            res[i] = digits[i - 1];
        }
        
        //个位数+1, 记录carry
        int carry = 0;
        res[res.length - 1] = res[res.length - 1] + 1;
        if (res[res.length - 1] >= 10) {
            carry = 1;
            res[res.length - 1] = res[res.length - 1] - 10;
        } else {
            carry = 0;
        }
        
        //更高的位数依次加上carry
        for (int i = res.length - 2; i >= 0; i--) {
            res[i] = res[i] + carry;
            if (res[i] >= 10) {
                carry = 1;
                res[i] = res[i] - 10;
            } else {
                carry = 0;
            }   
        }
        
        //如果最高位为0，删掉这一位；否则直接返回res
        if (res[0] != 0) {
            return res;
        } else {
            for (int i = 0; i < digits.length; i++) {
                digits[i] = res[i + 1];
            }
            return digits;
        }
    }
}
