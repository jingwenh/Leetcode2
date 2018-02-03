//在任意时候，添加括号的规则为：
//只有当左括号数量小于n时才加左括号
//只有当右括号数量小于左括号数量时才加右括号
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        helper(res, new StringBuilder(), 0, 0, n);
        return res;
    }
    
    private void helper(List<String> res, StringBuilder sb, int open, int close, int n) {
        if (sb.length() == n * 2) {
            res.add(new String(sb));
        }
        if (open < n) {
            sb.append("(");
            helper(res, sb, open + 1, close, n);
            sb.deleteCharAt(sb.length() - 1); //回溯
        }
        if (close < open) {
            sb.append(")");
            helper(res, sb, open, close + 1, n);
            sb.deleteCharAt(sb.length() - 1); //回溯
        }
    }
}
