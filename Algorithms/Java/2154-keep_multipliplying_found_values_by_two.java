class Solution {
    public int findFinalValue(int[] nums, int original) {

        HashSet<Integer> set = new HashSet<>();
        boolean flag = true;

        for(int i: nums){
            set.add(i);
            if(i == original) flag = false;
        }

        if(flag){
            return original;
        }

        while(set.contains(original)){
            original *=2;
        }

        return original;
    }
}