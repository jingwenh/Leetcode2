class Solution {
    public boolean isValidSudoku(char[][] board) {
        return (isRowValid(board) && isColumnValid(board) && isSubValid(board));
    }
    
    private boolean isRowValid(char[][] board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char num = board[i][j];
                Set<Character> set = new HashSet<>();
                if (set.contains(num) && num != '.') {
                    return false;
                } else {
                    set.add(num);
                }                
            }            
        }
        return true;
    }
    
    private boolean isColumnValid(char[][] board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char num = board[j][i];
                Set<Character> set = new HashSet<>();
                if (set.contains(num) && num != '.') {
                    return false;
                } else {
                    set.add(num);
                }                
            }            
        }
        return true;
    }
    
    private boolean isSubValid(char[][] board) {
        Set seen = new HashSet();
        for (int i=0; i<9; ++i) {
            for (int j=0; j<9; ++j) {
                char number = board[i][j];
                if (number != '.')
                    if (!seen.add(number + " in row " + i) ||
                        !seen.add(number + " in column " + j) ||
                        !seen.add(number + " in block " + i/3 + "-" + j/3))
                        return false;
            }
        }
        return true;
    }
}
