class Solution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int i = a.length() - 1, j = b.length() -1, carry = 0;
        while (i >= 0 || j >= 0) {
            int sum = carry;
            if (j >= 0) {
                sum = sum + b.charAt(j) - '0';
                j--;
            }
            if (i >= 0) {
                sum = sum + a.charAt(i) - '0';
                i--;
            } 
            sb.append(sum % 2);
            carry = sum / 2; //Sum >= 2时carry = 1, Sum < 2时carry = 0
        }
        if (carry != 0) sb.append(carry);
        return sb.reverse().toString();
    }
}
