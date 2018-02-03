class Solution {
    public String addBinary(String a, String b) {
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;
        StringBuilder res = new StringBuilder();
        while (i >= 0 || j >= 0) {
            int sum = carry;
            if (i >= 0) {
                sum = sum + a.charAt(i) - '0';
                i--;
            }
            if (j >= 0) {
                sum = sum + b.charAt(j) - '0'; // - '0'把字符转换成数字
                j--;
            }
            res.append(sum % 2 + "");//sum % 2可以得到对应的数位
            carry = sum / 2; //Sum >= 2时carry = 1, Sum < 2时carry = 0
        }
        
        //如果最后carry != 0要把carry加上
        if (carry != 0) {
            res.append("1");
        }
        return new String(res.reverse());
    }
}
