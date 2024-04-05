class Solution {
    public int uniqueMorseRepresentations(String[] words) {

        String code[] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        HashMap<Character, String> morseCode = new HashMap<>();
        HashSet<String> mySet =  new HashSet<>();
        String morse = "";
       
        for(char i = 'a'; i <= 'z'; i++){
            morseCode.put(i, code[i - 'a']);
        }

        for(String s: words){
            
            for(int i = 0; i < s.length(); i++){
                morse = morse + morseCode.get(s.charAt(i));
            
            }

           mySet.add(morse);
    
            morse = "";  
        }

        return mySet.size();
        
    }
}