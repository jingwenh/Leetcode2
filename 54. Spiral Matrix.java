//顺序：右 - 下 - 左 - 上
// [
//  [ 1, 2, 3 ],
//  [ 4, 5, 6 ],
//  [ 7, 8, 9 ]
// ]
//123 -> 69 -> 87 -> 4 -> 5
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>();
        if (matrix == null || matrix.length == 0 || matrix[0] == null || matrix[0].length == 0) {
            return res;
        }        
        
        int rowBegin = 0;
        int rowEnd = matrix.length - 1;
        int colBegin = 0;
        int colEnd = matrix[0].length - 1;
        
        //用rowBegin, rowEnd, colBegin, colEnd代替for循环里的常数值
        while (rowBegin <= rowEnd && colBegin <= colEnd) {
            //右，行不变列+
            for (int i = colBegin; i <= colEnd; i++) {
                res.add(matrix[rowBegin][i]);
            }
            rowBegin++;//一行结束，向下移一行（不然会重复从3开始）
            //下，列不变行+
            for (int i = rowBegin; i <= rowEnd; i++) {
                res.add(matrix[i][colEnd]);
            }
            colEnd--;//一列结束，向左移一列（同理，不然会重复9）
            //左，行不变列-
            if (rowBegin <= rowEnd) { //rowBegin先往右移，有可能在循环退出前就rowBegin > rowEnd, 这种情况会数组越界
                for (int i = colEnd; i >= colBegin; i--) {
                    res.add(matrix[rowEnd][i]);
                }
                rowEnd--; //一行结束，向上移以上
            }
            //上，列不变行-
            if (colBegin <= colEnd) {
                for (int i = rowEnd; i >= rowBegin; i--) {
                    res.add(matrix[i][colBegin]);
                }          
                colBegin++; //一列结束，向右移一列
            } 
        }
        
        return res;
    }
}
