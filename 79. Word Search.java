//dfs, 按照word的字母顺序在board上找字母
//用一个二维的boolean数组记录走过的节点
//当长度 == word.length() - 1时并且最后一个字母 == 单词的最后一个字母时返回true
class Solution {
    int[][] dirs = {
        {1, 0},
        {-1, 0},
        {0, 1},
        {0, -1}
    };
    public boolean exist(char[][] board, String word) {
        boolean[][] visited = new boolean[board.length][board[0].length];
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (dfs(word, 0, board, visited, i, j) == true) {
                    return true;
                }
            }
        }
        return false;
    }
    
    //cur记录当前已经找到了那个字母
    //int i, j记录已经在board上走到了哪个节点
    private boolean dfs(String word, int cur, char[][] board, boolean[][] visited, int i, int j) {
        if (visited[i][j] || word.charAt(cur) != board[i][j]) {
            return false;
        }
        if (cur == word.length() - 1) {
            return true;
        }        
        visited[i][j] = true;
        for (int[] dir : dirs) {
            int nx = i + dir[0];
            int ny = j + dir[1];
            //if inbound
            if (nx < 0 || nx >= board.length || ny < 0 || ny >= board[0].length) {
                continue;
            }
            if (dfs(word, cur + 1, board, visited, nx, ny)) {
                return true;
            }
        }
        visited[i][j] = false;
        return false;
    }
}
