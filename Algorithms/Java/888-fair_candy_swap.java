class Solution {
    public int[] fairCandySwap(int[] aliceSizes, int[] bobSizes) {

    HashSet<Integer> bobSet = new HashSet<>();
       int[] result = new int[2];

       int aliceTotal = 0;
       int bobTotal = 0;

       for(int i : aliceSizes){
        aliceTotal += i;
       }

       for(int i: bobSizes){
        bobTotal += i;
        bobSet.add(i);
       }

       //
       int delta = (bobTotal - aliceTotal)/2 ;

       for(int i: aliceSizes){
        if(bobSet.contains(delta + i)){
            result[0] = i;
            result[1] = delta + i;
            return result;
        }

       }

       return result;


        

    }
}