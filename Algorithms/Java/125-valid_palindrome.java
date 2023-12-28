class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;

        while(left < right){

        while( left < right && !isAlphaNumberic(s.charAt(left))){
            left++;
        }

        while(right > left && !isAlphaNumberic(s.charAt(right))){
            right--;
        }

        if(Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))){
           return false; 
        }

        left++;
        right--;

    }

       return true;
    }

    public static boolean isAlphaNumberic(char c){
        
        if((int)'A' <= (int)c && (int)c <= (int)'Z' || (int)'a' <= (int)c && (int)c <= (int)'z' || (int)'0' <= (int)c && (int)c <= (int)'9') {

            return true;
        }

        return false; 
    
    }
}