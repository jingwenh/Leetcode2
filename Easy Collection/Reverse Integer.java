//商余法取出每一个数位上的数，放进q里
//res = res * 10 + q.poll()得到反向的整数
//res要用long因为可能会溢出
//最后判断res是不是>Integer.MAX_VALUE，大于说明溢出了
//溢出时返回0
class Solution {
    public int reverse(int x) {
        //处理负数，把符号单独取出来，最后再加在结果上
        int sign = 1;
        if (x < 0) {
            sign = -1;
            x = x * (-1);
        }
        
        Queue<Integer> q = new LinkedList<>();
        while (x >= 1) {
            int remain = x % 10;
            q.offer(remain);
            x = x / 10;
        }
        
        long res = 0;
        while (!q.isEmpty()) {
            res = res * 10 + q.poll();
        }
        
        if (res > (long)Integer.MAX_VALUE) {
            return 0;
        }
        
        return (int)res * sign;
    }
}
