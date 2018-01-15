class Solution {
    //两个整数做XOR运算，结果有几位是1，结果就是几
    public int hammingDistance(int x, int y) {
        int xor = x ^ y, count = 0;
        for (int i=0;i<32;i++) count += (xor >> i) & 1;
        return count;
    }
}
