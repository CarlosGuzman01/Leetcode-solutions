class Solution {
    public int lengthOfLastWord(String s) {
        int counter = 0;
        int pointer = s.length() - 1;

       
            while (s.charAt(pointer) == ' ') {
                pointer--;

            }

            while(pointer >= 0 && s.charAt(pointer) != ' '){
                counter++;
                pointer--;
            }

            return counter;
        
    }
}