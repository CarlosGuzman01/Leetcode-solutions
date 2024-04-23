class Solution {
    public String truncateSentence(String s, int k) {

        String[] arr = s.split("\\W");
        StringBuilder sb = new StringBuilder();
        
        int i = 0;
        for(String sa:  arr){

            sb.append(sa + " ");

            if(i == k -1){
                break;
            }

            i++;
        }

        sb.deleteCharAt(sb.length() - 1);


        return sb.toString();
        
    }
}