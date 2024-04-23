class Solution {
    public int maximumWealth(int[][] accounts) {

        int max = 0;

        for(int[] r : accounts){
            int total = 0;
            for(int i : r){
                total = total + i;
            }

            max = Math.max(total, max);

        }

        return max;
        
    }
}