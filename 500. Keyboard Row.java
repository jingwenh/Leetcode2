import java.util.regex.*;
class Solution {
    public String[] findWords(String[] words) {
        String re1 = "[qwertyuiopQWERTYUIOP]+";
        String re2 = "[asdfghjklASDFGHJKL]+";
        String re3 = "[zxcvbnmZXCVBNM]+";
        //boolean isMatch = Pattern.matches(pattern, content);
        ArrayList<String> res = new ArrayList<>();
        for (String s : words) {
            if (Pattern.matches(re1, s) || Pattern.matches(re2, s) || Pattern.matches(re3, s)) {
                res.add(s);
            }
        }
        
        String[] result = new String[res.size()];
        int count = 0;
        for (String s : res) {
            result[count] = s;
            count++;
        }
        
        return result;
    }
}
