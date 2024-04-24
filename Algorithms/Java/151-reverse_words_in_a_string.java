class Solution {
    public String reverseWords(String s) {
        StringBuilder sb = new StringBuilder();

        String[] array = s.trim().split("\\s+");
    
        int i = array.length - 1;
        
        while(i >= 0){
            sb.append(array[i] + " ");
            i--;
        }

        sb.deleteCharAt(sb.length() - 1);
       
        return sb.toString();
        
    }
}