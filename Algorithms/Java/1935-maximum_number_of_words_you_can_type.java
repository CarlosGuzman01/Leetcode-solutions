class Solution {
    public int canBeTypedWords(String text, String brokenLetters) {

        HashSet<Character> mySet = new HashSet<>();
        int counter = 0;

        for(char c: brokenLetters.toCharArray()){
            mySet.add(c);
        }

        String[] arrStrings = text.split("\\W+");

        for(String s : arrStrings){
            counter++;
            System.out.println("counter: " + counter);
            for(char c : s.toCharArray()){
                if (mySet.contains(c)) {
                    counter--;
                    break;
                    
                }
            }
        }
        
        
        return counter;
        
    }
}