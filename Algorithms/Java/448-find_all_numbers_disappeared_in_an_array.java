class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {


        HashSet<Integer> mySet = new HashSet<>();
        ArrayList<Integer> list = new ArrayList<>();

        for(int i: nums){
            mySet.add(i);
        }

        for(int i = 1; i <= nums.length; i++){
            if(!mySet.contains(i)){
                list.add(i);
            }

        }

       return list;
        



    }
}