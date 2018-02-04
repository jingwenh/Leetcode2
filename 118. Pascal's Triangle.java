class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<>();
        
        if (numRows == 0) {
            return res;
        }
        
        List<Integer> one = new ArrayList<>();
        one.add(1);
        res.add(one);
        generateRow(res, numRows);
        return res;
    }
    
    private void generateRow(List<List<Integer>> res, int n) {
        //行数 = n时结束递归
        if (res.size() >= n) {
            return;
        }
        //两根指针做sliding window根据上一行生成下一行中间的数，然后在前后补1就得到下一行
        List<Integer> newRow = new ArrayList<>();
        int left = 0;
        int right = 1;
        newRow.add(1);
        List<Integer> pre = res.get(res.size() - 1);
        while (right < pre.size()) {
            newRow.add(pre.get(left) + pre.get(right));
            left++;
            right++;
        }
        newRow.add(1);
        res.add(newRow);
        generateRow(res, n);
    }
}
