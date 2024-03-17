class Solution {
    public int numJewelsInStones(String jewels, String stones) {

        int counter = 0;
        HashSet<Character> mySet = new HashSet<>();


        for(char c: jewels.toCharArray()){
            mySet.add(c);

        }

        for(char c: stones.toCharArray()){
            if (mySet.contains(c)) {
                counter++;
            }
        }

        return counter;
  
    }
}