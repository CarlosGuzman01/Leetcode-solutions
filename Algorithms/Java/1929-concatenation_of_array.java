class Solution {
    public int[] getConcatenation(int[] nums) {

        int[] answer =  new int[nums.length * 2];
        
        
        int j = 0;
        for(int i = 0; i < answer.length; i++){
            if(j > nums.length - 1) j = 0;
            answer[i] = nums[j];
            j++;
        }
        

        return answer;
        
    }
}