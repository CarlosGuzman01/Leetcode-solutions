class Solution {
    public int distributeCandies(int[] candyType) {

        HashSet<Integer> mySet = new HashSet<>();

        for(int i: candyType){

            if(candyType.length / 2 == mySet.size()) return mySet.size();

            mySet.add(i);
        }

        return mySet.size();
  
    }
}