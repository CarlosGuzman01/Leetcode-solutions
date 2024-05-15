class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        
        HashMap<Integer, Integer> myMap = new HashMap<>();
        HashSet<Integer> set = new HashSet<>();
        
        for(int i : nums1){
            myMap.put(i, 1);
            set.add(i);
        }

        for(int i: nums2){
            if(set.contains(i)){
                myMap.remove(i);
            }else{
                myMap.put(i, 2);
            }
        }

        ArrayList<Integer> list1 = new ArrayList<>();
        ArrayList<Integer> list2 = new ArrayList<>();
        ArrayList<List<Integer>> finalList = new ArrayList<>();

        for(int i: myMap.keySet()){
            if(myMap.get(i) == 1){
                list1.add(i);
            }else{
                list2.add(i);
            }
        }

        finalList.add(list1);
        finalList.add(list2);

        return finalList;
    }
}