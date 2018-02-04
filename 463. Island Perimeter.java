//只有一块island
//先统计有几个1，总边数 = 1的数量 * 4
//然后去掉中间夹着的边
//每有一条夹着的边，总边数 - 2
//从左向右遍历数组，判断1的右边和下边有没有1，有就总边数 - 2 （只统计右边和下边就不会重复统计）
class Solution {
    public int islandPerimeter(int[][] grid) {
        int peri = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    peri = peri + 4;
                    if (i <= grid.length - 2) {
                        if (grid[i + 1][j] == 1) {
                            peri = peri - 2;
                        }
                    }
                    if (j <= grid[0].length - 2) {
                        if (grid[i][j + 1] == 1) {
                            peri = peri - 2;
                        }
                    }
                }
            }
        }
        return peri;
    }
}
