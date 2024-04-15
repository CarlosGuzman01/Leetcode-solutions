class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        
        HashSet<Integer> mySet =  new HashSet<>();
        HashSet<Integer> setAnswer = new HashSet<>();
        

        for(int i: nums1){
            mySet.add(i);
        }

        for(int i: nums2){
            if (mySet.contains(i)) {
                setAnswer.add(i);
                
            }
        }

        int[] finalArr = new int[setAnswer.size()];

        int i = 0;
        for(int j: setAnswer){
            finalArr[i] = j;
            i++;
        }

        return finalArr;

        
    }
}