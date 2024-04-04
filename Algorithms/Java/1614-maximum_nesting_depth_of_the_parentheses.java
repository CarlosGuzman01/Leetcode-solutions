class Solution {
    public int maxDepth(String s) {

         
        int maxDepth = 0;
        int current = 0;
        
        for(char c: s.toCharArray()){
            if(c == '('){
                current += 1; 
            }else if(c == ')'){
                current -= 1;
            }

            maxDepth = Math.max(current, maxDepth);

        }

        return maxDepth;
        
    }
}