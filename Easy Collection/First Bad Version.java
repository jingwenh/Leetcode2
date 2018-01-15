/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */
//[O O O O X X X X X]
public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int start = 1;
        int end = n;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            //优先抛掉X，保留O
            if (isBadVersion(mid) == true) {
                end = mid;
            } else {
                start = mid;
            }
        }
        if (isBadVersion(start)) {
            return start;
        } else {
            return end;
        }
    }
}
