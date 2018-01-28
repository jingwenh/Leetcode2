//You can always win a Nim game if the number of stones nn in the pile is not divisible by 44.

class Solution {
    public boolean canWinNim(int n) {
        return (n % 4 != 0);
    }
}
