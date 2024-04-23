class Solution {
    public int finalValueAfterOperations(String[] operations) {

        int counter = 0;

        for(String s: operations){
            for(char c : s.toCharArray()){
                if(c == '+'){
                    counter++;
                    break;
                }else if(c == '-'){
                    counter--;
                    break;
                }
            }
        }

        return counter;
        
    }
}