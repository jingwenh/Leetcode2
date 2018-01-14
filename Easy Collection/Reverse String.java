class Solution {
    public String reverseString(String s) {
        Stack<String> stk = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            stk.push(s.charAt(i) + "");
        }
        
        StringBuilder res = new StringBuilder();
        while (!stk.isEmpty()) {
            res.append(stk.pop());
        }
        
        return new String(res);
    }
}
