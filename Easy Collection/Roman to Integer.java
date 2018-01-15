class Solution {
    //规律：左边的数字如果小于右边的数字 = 右 - 左
    //V = 5
    //IV = V - I = 5 - 1 = 4
    //VI = 5 + 1 = 6
    //罗马数字的和 = 每一位数字的值的和
    //每一位数字的值由自己本身和后面一位数决定
    //如果右边的数字大于本身这位数，那么这个数得值 = 这位数得值 - 右边的数字的值 * 2
    //比如：IIVI = 1 + 1 + (5-2) + 1 = 6
    public static int romanToInt(String s) {
        if (s == null || s.length() == 0) return 0;
        int res = toNumber(s.charAt(0));
        //从左往右遍历
        for (int i = 1; i < s.length(); i++) {
            //如果这个数大于后面的数
            //这个数的值 = 这个数 - 2 * 后面的数
            //因为遍历到下一位还要再加上一次后面的数
            //即 （这个数 - 2 * 后面的数）+ 后面的数 = 这两个数的值
            if (toNumber(s.charAt(i)) > toNumber(s.charAt(i - 1))) {
                res += toNumber(s.charAt(i)) - 2 * toNumber(s.charAt(i - 1));
            } else {
                res += toNumber(s.charAt(i));
            }
        }
        return res;
    }

    public static int toNumber(char c) {
        int res = 0;
        switch (c) {
            case 'I' : return 1;
            case 'V' : return 5;
            case 'X' : return 10;
            case 'L' : return 50;
            case 'C' : return 100;
            case 'D' : return 500;
            case 'M' : return 1000;
        }
        return res;
    }
}
