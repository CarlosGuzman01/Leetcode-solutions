class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        HashSet<Integer> mySet = new HashSet<>();
        ArrayList<Integer> list = new ArrayList<>();

        for(int i : nums1){
            mySet.add(i);
        }

        for(int i : nums2){
            if (mySet.contains(i)) {
                list.add(i);  
            }
        }

        Collections.sort(list);

        if(list.isEmpty()){
            return -1;
        }

        return list.get(0);
        
    }
}