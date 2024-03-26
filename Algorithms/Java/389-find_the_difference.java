class Solution {
    public char findTheDifference(String s, String t) {

          int sum = 0;
    
        for(char c: t.toCharArray()){
            sum = sum + (int) c;
        }

        for(char c: s.toCharArray()){
            sum = sum - (int) c; 
        }

        return (char) sum;
        
        
    }
}