class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        
        ArrayList<Integer> list = new ArrayList<>();
        int[] ans = new int[nums.length];
        
        for(int i = 0; i < nums.length; i++){
            list.add(index[i], nums[i]);
        }

        int j = 0;
        for(int i: list){
            ans[j] = i;
            j++;
        }

        return ans;

    }
}