class Solution {
    public boolean checkIfPangram(String sentence) {
        
        HashSet<Character> mySet1 = new HashSet<>();
        String letters = "qwertyuiopasdfghjklzxcvbnm";

        for(char c: sentence.toCharArray()){
            mySet1.add(c);
        }

        for(char c : letters.toCharArray()){
            if (!mySet1.contains(c)) {
                return false; 
            }
        }

        return true;
    }
    
}