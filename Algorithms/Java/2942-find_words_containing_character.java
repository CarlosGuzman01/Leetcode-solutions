class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {

        ArrayList<Integer> answer = new ArrayList<>();

        for(int i = 0; i < words.length; i++){

            for(char c : words[i].toCharArray()){
                if(c == x) {
                    answer.add(i);
                    break; 
                }
                 

            }
        }

        return answer;
        
    }
}