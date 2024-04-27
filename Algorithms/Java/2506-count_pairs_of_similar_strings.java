class Solution {
    public int similarPairs(String[] words) {

        int counterMax = 0;
        
        for(int i = 0; i < words.length; i++){
            counterMax = counterMax + helperCounter(words, i);
        }

        return counterMax;

        
    }

        public static int helperCounter(String words[], int i){
         
        HashSet<Character> mySet = new HashSet<>();
        HashSet<Character> mySet2 = new HashSet<>();
        int counter = 0;

        for(char c: words[i].toCharArray()){
            mySet.add(c);
        }

        for(int j = i + 1; j < words.length; j++){

            for(char c: words[j].toCharArray()){
                mySet2.add(c);
            }

            if (mySet.equals(mySet2)) {
                counter++;
            }

            mySet2.clear();


        }

        return counter;
    }


}