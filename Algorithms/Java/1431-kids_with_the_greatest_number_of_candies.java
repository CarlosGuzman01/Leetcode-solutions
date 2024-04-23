class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {

        ArrayList<Boolean> answer = new ArrayList<>();

        int max = 0;
        for(int i : candies){
            max = Math.max(i, max);
        }

        
        for(int i: candies){
            if(i + extraCandies >= max){
                answer.add(true);
            }else{
                answer.add(false);
            }
        }


        return answer;
        
    }
}