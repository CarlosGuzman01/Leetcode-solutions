class Solution {
    public int findMaxK(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        int candidate = -1;

        for(int i: nums){
            set.add(i);
        }
        
        for(int i: nums){
            if(i > candidate && set.contains(-i)){
                candidate = i;
            }

        }


        return candidate;

    }
}