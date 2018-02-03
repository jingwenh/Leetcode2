//因子里面有一个2和一个5可以多一个0
//阶乘里面5更多
//只用数5的个数
class Solution {
    public int trailingZeroes(int n) {
        int res = 0;
        while (n >= 5) {
            n = n / 5;
            res = res + n;
        }
        return res;
    }
}
