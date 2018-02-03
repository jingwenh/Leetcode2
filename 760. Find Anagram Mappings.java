class Solution {
    public int[] anagramMappings(int[] A, int[] B) {
        //Map from value to index of B
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < B.length; i++) {
            map.put(B[i], i);
        }
        
        ArrayList<Integer> res = new ArrayList<>();
        for (int i : A) {
            res.add(map.get(i));
        }
        
        for (int i = 0; i < A.length; i++) {
            A[i] = res.get(i);
        }
        
        return A;
    }
}
