class Solution {
    public int countNegatives(int[][] grid) {

        int counter = 0;

        for(int[] a : grid){
            for(int i = a.length - 1; i >= 0; i--){
                if(a[i] >= 0){
                    break;
                }

                System.out.println(a[i]);

                counter++;

            }

        }

        return counter;
        
    }
}