class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int n = grid.length;
        HashSet<Integer> mySet = new HashSet<>();
        int[] result = new int[2];

        for(int[] row : grid){
            for(int i : row){
                if(mySet.contains(i)){
                    result[0] = i;  
                }
                
                mySet.add(i);
            }
        }

        for(int i = 1; i <= n * n; i++){
            if(!mySet.contains(i)){
                result[1] = i;
                return result;
            }
        }


        return result;
        
    }
}