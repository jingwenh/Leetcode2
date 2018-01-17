class Solution {
    public void setZeroes(int[][] matrix) {
        Queue<Coordinate> q = new LinkedList<>();
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length;j++) {
                if (matrix[i][j] == 0) {
                    q.add(new Coordinate(i, j));
                }
            }
        }
        while (!q.isEmpty()) {
            Coordinate c = q.poll();
            setZero(matrix, c.row, c.col);
        }
    }
    
    //把对应行列都设成0
    private void setZero(int[][] matrix, int row_no, int col_no) {
        for (int i = 0; i < matrix[0].length; i++) {
            matrix[row_no][i] = 0;
        }
        for (int i = 0; i < matrix.length; i++) {
            matrix[i][col_no] = 0;
        }
    }
    
    private class Coordinate {
        int row;
        int col;
        Coordinate (int row, int col) {
            this.row = row;
            this.col = col;
        }
    }
}
