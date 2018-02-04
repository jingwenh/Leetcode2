//类似Spiral Matrix I
//把读换成写
// [
//  [ 1, 2, 3 ],
//  [ 8, 9, 4 ],
//  [ 7, 6, 5 ]
// ]
//顺序：右 - 下 - 左 - 上
//第一层循环顺序：123 - 45 - 67 - 8
class Solution {
    public int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];
        int rowBegin = 0;
        int rowEnd = n - 1;
        int colBegin = 0;
        int colEnd = n - 1;
        
        int count = 1;
        while (rowBegin <= rowEnd && colBegin <= colEnd) {
            //右, 行不变列++
            for (int i = colBegin; i <= colEnd; i++) {
                matrix[rowBegin][i] = count;
                count++;
            }
            rowBegin++;
            //下，列不变行++
            for (int i = rowBegin; i <= rowEnd; i++) {
                matrix[i][colEnd] = count;
                count++;
            }
            colEnd--;
            //左, 行不变列--
            if (rowBegin <= rowEnd) {
                for (int i = colEnd; i >= colBegin; i--) {
                    matrix[rowEnd][i] = count;
                    count++;
                }     
                rowEnd--;
            }
            //上，列不变行--
            if (colBegin <= colEnd) {
                for (int i = rowEnd; i >= rowBegin; i--) {
                    matrix[i][colBegin] = count;
                    count++;
                }
                colBegin++;               
            }
        }
        return matrix;
    }
}
