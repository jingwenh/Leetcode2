//Better solution
class Solution {
    public boolean validPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        while (left <= right) {
            if (s.charAt(left) != s.charAt(right)) {
                return helper(s, left + 1, right) || helper(s, left, right - 1); //去掉左端点或者去掉右端点判断是不是回文
            } else {
                left++;
                right--;
            }
        }
        return true;
    }
    
    //判断从left到right是不是回文
    private boolean helper(String s, int left, int right) {
        while (left <= right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            } else {
                left++;
                right--;
            }
        }
        return true;
    }
}


/*----------------------------------------------------------------------------------------------------*/

//相向双指针
//第一次到两端不相等时出来，取出中间那一段字符串
//第一次去掉左端点，判断是不是回文
//第二次去掉右端点，判断是不是回文
class Solution {
    public boolean validPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        boolean flag = true;
        while (left <= right) {
            if (s.charAt(left) == s.charAt(right)) {
                left++;
                right--;
            } else {
                flag = false;
                break;
            }
        }
        if (flag == true) {
            return true;
        }
        
        String sub = s.substring(left, right + 1);
        System.out.println(sub);
        left = 0;
        right = sub.length() - 2;
        flag = true;
        while (left <= right) {
            if (sub.charAt(left) != sub.charAt(right)) {
                flag = false;
                break;
            } else {
                left++;
                right--;
            }
        }
        if (flag == true) {
            return true;
        }
        
        left = 1;
        right = sub.length() - 1;        
        flag = true;
        while (left <= right) {
            if (sub.charAt(left) != sub.charAt(right)) {
                System.out.println(s.charAt(left) + " != " + s.charAt(right));
                flag = false;
                break;
            } else {
                left++;
                right--;
            }
        }        
        return flag;
    }
}
