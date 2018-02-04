// [
//   [1,2,3],
//   [4,5,6],
//   [7,8,9]
// ],
//沿对角线交换------>
// [
//   [1,4,7],
//   [2,5,8],
//   [3,6,9]
// ],
//每行reverse------>
// [
//   [7,4,1],
//   [8,5,2],
//   [9,6,3]
// ],
class Solution {
    public void rotate(int[][] matrix) {
        //沿对角线交换
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < i; j++) { //只换对角线的一边，换两边就换回来了, j < i表示把对角线左边换到右边
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        
        //每行reverse
        for (int[] row : matrix) {
            int left = 0;
            int right = row.length - 1;
            while (left <= right) {
                int temp  = row[left];
                row[left] = row[right];
                row[right] = temp;
                left++;
                right--;
            }
        }
    }
}
